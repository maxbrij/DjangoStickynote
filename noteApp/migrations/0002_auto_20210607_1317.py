# Generated by Django 3.2.3 on 2021-06-07 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Address',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='Country',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='Pin',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AddField(
            model_name='user',
            name='State',
            field=models.CharField(default='', max_length=20),
        ),
    ]
