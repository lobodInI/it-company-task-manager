# Generated by Django 4.2.7 on 2023-11-10 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='worker',
            options={'verbose_name': 'worker', 'verbose_name_plural': 'workers'},
        ),
    ]
