# Generated by Django 4.2.6 on 2023-11-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter_service', '0003_remove_mailing_client_mailing_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='surname',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Фамилия'),
        ),
    ]
