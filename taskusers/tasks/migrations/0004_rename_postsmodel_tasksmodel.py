# Generated by Django 4.2.6 on 2023-10-11 13:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_postsmodel_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostsModel',
            new_name='TasksModel',
        ),
    ]
