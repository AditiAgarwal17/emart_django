# Generated by Django 3.2.3 on 2021-05-29 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210529_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
