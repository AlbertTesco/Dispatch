from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogPostListView, BlogPostCreatView, BlogPostDetailView, BlogPostUpdateView, BlogPostDeleteView

app_name = BlogConfig.name
urlpatterns = [
                  path('all/', BlogPostListView.as_view(), name='blog_list'),
                  path('create_post/', BlogPostCreatView.as_view(), name='post_create'),
                  path('detail/<slug:slug>/', BlogPostDetailView.as_view(), name='blog_post_detail'),
                  path('update/<slug:slug>/', BlogPostUpdateView.as_view(), name='blog_post_update'),
                  path('delete/<slug:slug>/', BlogPostDeleteView.as_view(), name='blog_post_delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
