# Generated by Django 2.1.4 on 2020-05-02 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0010_auto_20200502_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='date',
        ),
    ]