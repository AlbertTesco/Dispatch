from django.urls import path, include

urlpatterns = [
    path('', include('newsletter_service.urls', namespace='newsletter_service')),
]
