# Generated by Django 3.0.8 on 2020-07-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200704_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Qaralama olaraq yadda saxlanilsin?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Mezmun'),
        ),
        migrations.AlterField(
            model_name='post',
            name='titles',
            field=models.CharField(max_length=120, verbose_name='Bashliq'),
        ),
    ]
