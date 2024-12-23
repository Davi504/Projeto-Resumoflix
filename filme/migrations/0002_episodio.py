# Generated by Django 5.1.4 on 2024-12-23 01:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodios', to='filme.filme')),
            ],
        ),
    ]
