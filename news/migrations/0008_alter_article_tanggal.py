# Generated by Django 5.0.1 on 2024-01-30 09:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_komentar_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tanggal',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
