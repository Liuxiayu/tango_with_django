# Generated by Django 2.1.3 on 2018-11-20 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20181120_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='theme',
            field=models.CharField(max_length=64),
        ),
    ]
