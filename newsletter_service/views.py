from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from newsletter_service.forms import ClientForm, MailingMessageCreateForm, MailingCreateForm
from newsletter_service.models import Client, Message, Mailing, MailingLog


def managers_required(user):
    return user.groups.filter(name='Managers').exists() or user.is_superuser


# Client Controllers
@login_required
def get_clients_page(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'newsletter_service/clients.html', context)


def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newsletter_service:clients')  # Перенаправление на страницу успешного добавления
    else:
        form = ClientForm()

    return render(request, 'newsletter_service/add_client.html', {'form': form})


@user_passes_test(managers_required)
def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    if request.method == 'POST':
        client.delete()
        return redirect('newsletter_service:clients')

    return render(request, 'newsletter_service/delete_client.html', {'client': client})


# --------------------------------

# Mailing Controllers
@login_required
def create_mailing(request):
    """Создание рассылки"""
    MailingFormSet = modelformset_factory(Message, form=MailingMessageCreateForm, extra=1)

    if request.method == 'POST':
        mailing_form = MailingCreateForm(request.POST)
        formset = MailingFormSet(request.POST, queryset=Message.objects.none())

        if mailing_form.is_valid() and formset.is_valid():
            mailing = mailing_form.save(commit=False)
            mailing.status = 'created'
            mailing.save()

            selected_clients = request.POST.getlist('client')
            clients = Client.objects.filter(pk__in=selected_clients)

            instances = formset.save(commit=False)
            for instance in instances:
                instance.mailing = mailing
                instance.save()

            mailing.client.set(clients)  # Привязываем клиентов к рассылке
            return redirect('newsletter_service:mailing_list')
    else:
        mailing_form = MailingCreateForm()
        formset = MailingFormSet(queryset=Message.objects.none())

    context = {
        'mailing_form': mailing_form,
        'formset': formset,
    }
    return render(request, 'newsletter_service/creation_mailing.html', context)


def delete_mailing(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)

    if request.method == 'GET':
        mailing.delete()
        return redirect('newsletter_service:mailing_list')  # Перенаправление на страницу mailing_list

    context = {'mailing': mailing}
    return redirect('newsletter_service:mailing_list')  # Перенаправление на страницу mailing_list


@login_required
def get_list_mailing(request):
    """Вывод на форму все доступные рассылки"""
    mailing = Mailing.objects.all()
    context = {
        'mailings': mailing
    }
    return render(request, 'newsletter_service/mailing_list.html', context)


@login_required
def send_mailing(request, pk):
    try:
        mailing = Mailing.objects.get(id=pk)
    except Mailing.DoesNotExist:
        return HttpResponse("Рассылка не найдена")

    if mailing.status == 'created' or mailing.status == 'completed':
        print("Changed to start")
        mailing.status = 'started'
        mailing.save()
        MailingLog.objects.create(mailing=mailing, status='Changed', server_response='Mailing has been launched')

    else:
        print("Changed to stop")
        mailing.status = 'completed'
        mailing.save()
        MailingLog.objects.create(mailing=mailing, status='Changed', server_response='Mailing has been suspended')

    return redirect('newsletter_service:mailing_list')


# --------------------------------

# Logs controllers

def mailing_log_view(request):
    logs = MailingLog.objects.all()
    return render(request, 'newsletter_service/mailing_log.html', {'logs': logs})
