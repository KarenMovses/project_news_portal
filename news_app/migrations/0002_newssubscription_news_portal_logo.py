# Generated by Django 4.0.5 on 2022-06-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newssubscription',
            name='news_portal_logo',
            field=models.URLField(null=True),
        ),
    ]
