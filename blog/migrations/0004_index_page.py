# Generated by Django 2.1.3 on 2018-11-11 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181111_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_num', models.IntegerField(default=0, verbose_name='浏览量')),
            ],
        ),
    ]