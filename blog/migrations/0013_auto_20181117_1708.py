# Generated by Django 2.1.3 on 2018-11-17 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_read_read_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='read',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test', to='blog.Article'),
        ),
    ]
