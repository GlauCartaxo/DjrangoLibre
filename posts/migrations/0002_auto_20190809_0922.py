# Generated by Django 2.2.4 on 2019-08-09 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PostsFromUser', to=settings.AUTH_USER_MODEL, verbose_name='autor'),
        ),
    ]
