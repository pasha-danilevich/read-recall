# Generated by Django 5.0.4 on 2024-08-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0021_rename_type_training_type_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartOfSpeech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='synonym',
            old_name='part_of_speech',
            new_name='part_of_speech_name',
        ),
        migrations.RenameField(
            model_name='translation',
            old_name='part_of_speech',
            new_name='part_of_speech_name',
        ),
        migrations.RenameField(
            model_name='word',
            old_name='part_of_speech',
            new_name='part_of_speech_name',
        ),
    ]
