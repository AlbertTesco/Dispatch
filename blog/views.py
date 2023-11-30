# Create your views here.


from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import BlogPost
from blog.services import cache_blog


class BlogPostListView(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'blog/blog_posts_list.html'
    context_object_name = "posts"
    extra_context = {"title": "Блог"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем данные из вашей функции cache_mailing
        mailing_list = cache_blog()  # Предположим, что функция cache_mailing определена

        # Добавляем данные в контекст представления
        context['mailing_list'] = mailing_list
        return context


class BlogPostCreatView(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = 'blog/blog_posts_form.html'
    fields = ('title', 'content')
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)


class BlogPostDetailView(LoginRequiredMixin, DetailView):
    model = BlogPost
    template_name = 'blog/blog_post_detail.html'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    template_name = 'blog/blog_posts_form.html'
    fields = ('title', 'content')
    success_url = reverse_lazy('blog:blog_list')


class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/blog_post_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')
