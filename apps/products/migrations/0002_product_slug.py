# Generated by Django 5.0.1 on 2024-02-11 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
