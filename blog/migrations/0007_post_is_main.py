# Generated by Django 4.2.11 on 2024-04-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
