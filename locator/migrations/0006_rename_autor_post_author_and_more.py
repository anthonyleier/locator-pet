# Generated by Django 4.1.2 on 2022-10-07 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0005_alter_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='autor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='descricao',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='imagem1',
            new_name='image1',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='imagem2',
            new_name='image2',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='imagem3',
            new_name='image3',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publicado',
            new_name='published',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='titulo',
            new_name='title',
        ),
    ]
