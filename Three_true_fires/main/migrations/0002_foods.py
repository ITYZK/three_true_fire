# Generated by Django 2.2.5 on 2019-10-06 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='foods',
            fields=[
                ('fid', models.IntegerField(auto_created=1000, max_length=10, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=255, unique=True)),
                ('price', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=11)),
                ('number', models.IntegerField(max_length=11)),
                ('ftype', models.CharField(max_length=30)),
                ('img_path', models.CharField(max_length=50)),
            ],
        ),
    ]