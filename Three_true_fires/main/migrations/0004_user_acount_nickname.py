# Generated by Django 2.2.5 on 2019-10-06 12:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20191006_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_acount',
            name='nickname',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
