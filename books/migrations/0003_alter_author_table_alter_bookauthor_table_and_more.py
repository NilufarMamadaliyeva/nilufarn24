# Generated by Django 5.0.1 on 2024-01-23 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='author',
            table='author_table',
        ),
        migrations.AlterModelTable(
            name='bookauthor',
            table='bookauthor_table',
        ),
        migrations.AlterModelTable(
            name='bookreview',
            table='review',
        ),
    ]