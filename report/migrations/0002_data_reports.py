# Generated by Django 2.1.4 on 2020-05-02 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='reports',
            field=models.CharField(choices=[('DAILY', 'FR'), ('WEEKLY', 'SO'), ('MONTHLY', 'JR')], default='CR', max_length=2),
        ),
    ]
