# Generated by Django 2.1.3 on 2018-11-16 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_auto_20181115_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheese',
            name='image',
            field=models.FileField(blank=True, upload_to='post_image'),
        ),
    ]
