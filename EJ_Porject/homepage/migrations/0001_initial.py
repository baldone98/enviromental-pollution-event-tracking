# Generated by Django 5.0.3 on 2024-04-23 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_text', models.CharField(max_length=255)),
                ('date_fetched', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
