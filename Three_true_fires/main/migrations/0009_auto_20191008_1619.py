# Generated by Django 2.2.5 on 2019-10-08 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20191007_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='nickname',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
