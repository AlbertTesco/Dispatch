from django.conf import settings
from django.core.cache import cache

from .models import BlogPost


def cache_blog() -> list:
    if settings.CACHE_ENABLED:
        key = 'blog_list'
        blog_list = cache.get(key)
        if blog_list is None or len(blog_list) != BlogPost.objects.all().count():
            blog_list = BlogPost.objects.all()
            cache.set(key, blog_list)
    else:
        blog_list = BlogPost.objects.all()

    return blog_list
