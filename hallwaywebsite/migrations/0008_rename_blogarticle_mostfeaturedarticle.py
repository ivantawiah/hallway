# Generated by Django 5.1.5 on 2025-01-27 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hallwaywebsite', '0007_rename_hallwayevents_hallwayevent_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogArticle',
            new_name='MostFeaturedArticle',
        ),
    ]
