# Generated by Django 4.1.1 on 2022-10-05 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0004_post_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
