# Generated by Django 3.2.8 on 2022-05-19 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_fileinfo_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyinfo',
            name='daily_time',
            field=models.DateTimeField(auto_now=True, verbose_name='推荐时间'),
        ),
    ]
