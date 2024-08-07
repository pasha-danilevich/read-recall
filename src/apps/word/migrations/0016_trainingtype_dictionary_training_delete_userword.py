# Generated by Django 5.0.4 on 2024-07-13 23:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0015_alter_word_text'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words', to=settings.AUTH_USER_MODEL)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='word.word')),
            ],
            options={
                'unique_together': {('user', 'word')},
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lvl', models.IntegerField(default=1, verbose_name='lvl')),
                ('time', models.IntegerField(verbose_name='time')),
                ('dictionary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training', to='word.dictionary')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='training', to='word.trainingtype')),
            ],
        ),
        migrations.DeleteModel(
            name='UserWord',
        ),
    ]
