# Generated by Django 3.2.7 on 2021-09-27 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20210924_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='story',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]