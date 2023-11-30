from django import forms

from .models import Client, Mailing, Message


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MailingCreateForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['send_time', 'frequency', 'client']
        widgets = {
            'send_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }


class MailingMessageCreateForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body']
        widgets = {
            'subject': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'body': forms.Textarea(attrs={'required': True, 'class': 'form-control'})
        }
# class MailingCreateForm(forms.ModelForm):
#     class Meta:
#         model = Mailing
#         fields = ['send_time', 'frequency', 'client']
#         widgets = {
#             'send_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
#             'frequency': forms.TextInput(attrs={'class': 'form-control'}),  # Пример для поля frequency
#             'client': forms.Select(attrs={'class': 'form-control'}),  # Пример для поля client
#         }
#
#
# class MailingMessageCreateForm(forms.ModelForm):
#     class Meta:
#         model = Message
#         fields = ['subject', 'body']
#         widgets = {
#             'subject': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
#             'body': forms.Textarea(attrs={'required': True, 'class': 'form-control'}),
#         }
