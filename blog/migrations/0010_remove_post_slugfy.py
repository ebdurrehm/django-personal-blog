# Generated by Django 3.0.8 on 2020-07-10 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_slugfy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slugfy',
        ),
    ]
