# Generated by Django 5.1.4 on 2024-12-23 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0002_episodio'),
    ]

    operations = [
        migrations.AddField(
            model_name='episodio',
            name='video',
            field=models.URLField(default='http://default.url'),
        ),
    ]