# Generated by Django 2.2 on 2020-01-01 14:26

import DeepLearningForum.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeepLearningForum', '0011_auto_20200101_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='static/img/avatar/default.png', max_length=200, storage=DeepLearningForum.storage.ImageStorage(), upload_to='static/img/avatar/%Y/%m', verbose_name='用户头像'),
        ),
    ]
