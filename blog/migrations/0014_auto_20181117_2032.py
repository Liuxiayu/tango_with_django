# Generated by Django 2.1.3 on 2018-11-17 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20181117_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='today_read_num',
            field=models.IntegerField(default=0, verbose_name='今日阅读数'),
        ),
        migrations.AlterField(
            model_name='read',
            name='read_num',
            field=models.IntegerField(default=1, verbose_name='浏览量'),
        ),
    ]
