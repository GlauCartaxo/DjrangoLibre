# Generated by Django 2.2.4 on 2019-08-09 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_posts_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='posts'),
        ),
    ]