from django.db import models


class Client(models.Model):
    email = models.EmailField(verbose_name="Эл.почта")
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    comment = models.TextField(verbose_name="Комментарий")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Mailing(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    send_time = models.DateTimeField(auto_now_add=True, verbose_name="Время отправки")

    frequency_choices = [
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ]
    frequency = models.CharField(max_length=10, choices=frequency_choices, verbose_name="Рассылка")

    status_choices = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, verbose_name="Статус")


class Message(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name="Рассылка")
    subject = models.CharField(max_length=255, verbose_name="Тема письма")
    body = models.TextField(verbose_name="Содержание письма")


class MailingLog(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name="Рассылка")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время последней попытки")
    status = models.CharField(max_length=10, verbose_name="Статус попытки")
    server_response = models.TextField(verbose_name="Ответ почтового сервера")
