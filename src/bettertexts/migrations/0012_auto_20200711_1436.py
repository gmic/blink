# Generated by Django 3.0.8 on 2020-07-11 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bettertexts', '0011_auto_20200527_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='range',
            field=models.PositiveIntegerField(default=5, verbose_name='range'),
        ),
    ]
