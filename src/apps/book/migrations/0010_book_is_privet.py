# Generated by Django 5.0.4 on 2024-08-20 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_alter_book_author_alter_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_privet',
            field=models.BooleanField(default=False),
        ),
    ]