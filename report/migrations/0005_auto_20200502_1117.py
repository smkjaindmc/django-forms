# Generated by Django 2.1.4 on 2020-05-02 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_auto_20200502_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='concern',
            field=models.TextField(default='your answer'),
        ),
        migrations.AddField(
            model_name='data',
            name='next_doc',
            field=models.FileField(null=True, upload_to='cv/images/'),
        ),
        migrations.AddField(
            model_name='data',
            name='next_plan',
            field=models.TextField(default='your answer'),
        ),
    ]
