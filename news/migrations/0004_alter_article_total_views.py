# Generated by Django 5.0.1 on 2024-01-25 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_article_total_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='total_views',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
