# Generated by Django 5.0.4 on 2024-08-10 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0022_partofspeech_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='synonym',
            name='part_of_speech',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='synonyms', to='word.partofspeech'),
        ),
        migrations.AddField(
            model_name='translation',
            name='part_of_speech',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='translations', to='word.partofspeech'),
        ),
        migrations.AddField(
            model_name='word',
            name='part_of_speech',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='words', to='word.partofspeech'),
        ),
    ]
