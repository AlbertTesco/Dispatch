# Generated by Django 4.2.6 on 2023-10-31 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter_service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='full_name',
        ),
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='client',
            name='patronymic',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='client',
            name='surname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
