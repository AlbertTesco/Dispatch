# Create your views here.
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from users.forms import UserRegistrationForm, UserConfirmingEmailForm
from users.models import User


def managers_required(user):
    return user.groups.filter(name='Managers').exists() or user.is_superuser


class LoginView(BaseLoginView):
    """Вход в учетную запись"""
    template_name = 'users/login.html'

    def form_valid(self, form):
        user = form.get_user()

        # Проверяем, подтверждена ли почта пользователя
        if not user.verified:
            # Перенаправляем на страницу подтверждения почты
            return redirect(reverse('users:confirming', args=[user.id]))

        return super().form_valid(form)


class LogoutView(BaseLogoutView):
    """
    Выход из учетной записи
    """
    pass


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.generate_verification_code()
            user.send_verification_code()
            user.save()
            return redirect(reverse('users:confirming', kwargs={'pk': user.pk}))
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})


def user_confirm(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        form = UserConfirmingEmailForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            entered_code = form.cleaned_data.get('confirmation_code')
            if entered_code == user.verification_code:
                user.activate_user()
                user.save()
                return redirect(reverse('users:login'))
    else:
        form = UserConfirmingEmailForm()

    return render(request, 'users/email_confirmed.html', {'form': form, 'pk': pk})


@user_passes_test(managers_required)
def users_list(request):
    users = User.objects.all()
    return render(request, 'users/users_list.html', {'users': users})


@user_passes_test(managers_required)
def activate_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.activate_user()
    return redirect('users:list_users')  # Укажите нужный URL-путь для перенаправления после активации


@user_passes_test(managers_required)
def deactivate_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.deactivate_user()
    return redirect('users:list_users')
