# Generated by Django 5.1.7 on 2025-04-12 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0006_image_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
