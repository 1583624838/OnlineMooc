# Generated by Django 3.1.2 on 2020-10-07 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0004_auto_20201007_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='consult',
            name='userid',
            field=models.CharField(blank=True, default='1', max_length=255, null=True, verbose_name='用户id'),
        ),
    ]