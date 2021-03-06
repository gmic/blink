# Generated by Django 3.0.8 on 2020-09-06 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bettertexts', '0012_auto_20200711_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.CharField(blank=True, max_length=1000, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='question',
            name='rating_type',
            field=models.CharField(choices=[('S', 'Sterren'), ('P', 'Punten')], default='S', max_length=2, verbose_name='type'),
        ),
        migrations.AddField(
            model_name='type',
            name='comment_form_intro',
            field=models.TextField(blank=True, max_length=20000, verbose_name='comment form intro'),
        ),
        migrations.AddField(
            model_name='type',
            name='inform_label',
            field=models.CharField(blank=True, max_length=200, verbose_name='inform label'),
        ),
        migrations.AddField(
            model_name='type',
            name='involved_label',
            field=models.CharField(blank=True, max_length=200, verbose_name='involved label'),
        ),
        migrations.AddField(
            model_name='type',
            name='thanks',
            field=models.CharField(blank=True, default='Bedankt voor je reactie!', max_length=2000, verbose_name='thanks text'),
        ),
    ]
