# Generated by Django 5.0.3 on 2024-04-30 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_remove_searchquery_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchquery',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
