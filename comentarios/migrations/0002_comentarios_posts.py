# Generated by Django 2.2.4 on 2019-08-07 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comentarios', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='posts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Posts', verbose_name='posts'),
        ),
    ]