# Generated by Django 4.1.3 on 2022-11-25 10:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todolistitem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistitem',
            name='date1',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todolistitem',
            name='priority',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
