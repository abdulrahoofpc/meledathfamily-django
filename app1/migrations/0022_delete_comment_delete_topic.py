# Generated by Django 5.2 on 2025-05-12 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_comment_topic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
