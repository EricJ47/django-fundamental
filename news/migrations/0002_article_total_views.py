# Generated by Django 5.0.1 on 2024-01-25 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='total_views',
            field=models.IntegerField(null=True),
        ),
    ]