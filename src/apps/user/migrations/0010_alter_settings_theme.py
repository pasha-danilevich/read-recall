# Generated by Django 5.0.4 on 2024-08-09 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_delete_userbookrelation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='theme',
            field=models.CharField(choices=[('light', 'Светлая'), ('dark', 'Темная'), ('red', 'Красная'), ('green', 'Зеленая')], default=None, max_length=20, null=True),
        ),
    ]
