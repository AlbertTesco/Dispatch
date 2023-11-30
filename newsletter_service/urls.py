from django.urls import path
from django.views.decorators.cache import cache_page

from newsletter_service.apps import NewsletterServiceConfig
from newsletter_service.views import get_clients_page, add_client, create_mailing, get_list_mailing, delete_client, \
    send_mailing, mailing_log_view, delete_mailing

app_name = NewsletterServiceConfig.name

urlpatterns = [
    path('', get_list_mailing, name='mailing_list'),
    path('logs/', mailing_log_view, name='list_logs'),
    path('clients/', get_clients_page, name='clients'),
    path('clients/delete/<int:client_id>', delete_client, name='delete_client'),
    path('clients/add_client/', cache_page(60 * 15)(add_client), name='add_client'),
    path('create_mailing/', create_mailing, name='create_mailing'),
    path('send_mailing/<int:pk>/', send_mailing, name='send_mailing'),
    path('delete_mailing/<int:pk>/', delete_mailing, name='delete_mailing'),
]
