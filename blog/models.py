from django.db import models

NULLABLE = {
    'blank': True,
    'null': True,
}


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlogPost(TimeStampedModel):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.CharField(max_length=100)
    content = models.TextField(verbose_name="Содержание")
    preview = models.ImageField(upload_to="blog/", *NULLABLE)
    is_published = models.BooleanField(default=False)
    view_counter = models.IntegerField(default=0, verbose_name="Количество просмотров")

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"

    def __str__(self):
        return self.title
