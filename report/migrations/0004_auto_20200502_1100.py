# Generated by Django 2.1.4 on 2020-05-02 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20200502_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='hours',
            field=models.DecimalField(decimal_places=1, default=2, max_digits=2),
        ),
        migrations.AddField(
            model_name='data',
            name='today_doc',
            field=models.FileField(null=True, upload_to='cv/images/'),
        ),
        migrations.AddField(
            model_name='data',
            name='today_progress',
            field=models.TextField(default='add'),
        ),
    ]
