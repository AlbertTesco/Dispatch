from django.contrib import admin

from .models import Client, Mailing, Message, MailingLog


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'comment')
    search_fields = ('full_name', 'email')
    list_filter = ('full_name', 'email')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('client', 'send_time', 'frequency', 'status')
    list_filter = ('client', 'send_time', 'frequency', 'status')


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
