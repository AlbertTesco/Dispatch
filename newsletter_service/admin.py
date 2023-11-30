from django.contrib import admin

from .models import Client, Mailing, Message, MailingLog


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic', 'email', 'comment')
    search_fields = ('name', 'surname', 'patronymic', 'email')
    list_filter = ('name', 'surname', 'patronymic', 'email')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'send_time', 'frequency', 'status',)
    list_filter = ('id', 'send_time', 'frequency', 'status',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'subject', 'body')
    search_fields = ('subject',)
    list_filter = ('mailing',)


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'timestamp', 'status', 'server_response')
    search_fields = ('mailing__client__full_name', 'status')
    list_filter = ('mailing', 'status')
