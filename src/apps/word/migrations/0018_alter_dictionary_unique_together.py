# Generated by Django 5.0.4 on 2024-07-13 23:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0017_dictionary_translation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dictionary',
            unique_together={('user', 'word', 'translation')},
        ),
    ]
