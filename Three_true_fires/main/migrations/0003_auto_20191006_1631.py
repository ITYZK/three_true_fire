# Generated by Django 2.2.5 on 2019-10-06 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_foods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='fid',
            field=models.AutoField(auto_created=1000, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='foods',
            name='number',
            field=models.IntegerField(),
        ),
    ]
