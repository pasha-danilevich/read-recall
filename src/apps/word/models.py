from datetime import datetime, timedelta
from typing import cast
from django.db import models

from apps.word.managers import DictionaryCustomManager, DictionaryQuerySet

from .utils import get_current_unix_time
from config.settings import TRAINING_TYPES

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


class Word(models.Model):
    text = models.CharField(max_length=100, unique=True)
    part_of_speech = models.CharField(
        max_length=100, null=True, blank=True)  # Часть речи
    transcription = models.CharField(
        max_length=100, null=True, blank=True)  # Транскрипция

    translations: 'Translation'
    synonyms: 'Synonym'
    meanings: 'Meaning'
    dictionary: 'DictionaryQuerySet'
    
    def __str__(self):
        return self.text


class Translation(models.Model):
    word = models.ForeignKey(
        Word, on_delete=models.CASCADE, related_name='translations')
    text = models.CharField(max_length=100)
    part_of_speech = models.CharField(
        max_length=100, null=True, blank=True)  # Часть речи
    gender = models.CharField(max_length=10, null=True, blank=True)  # Род
    frequency = models.IntegerField(
        null=True, blank=True)  # Частота использования

    def __str__(self):
        return self.text


class Synonym(models.Model):
    word = models.ForeignKey(
        Word, on_delete=models.CASCADE, related_name='synonyms')
    text = models.CharField(max_length=100)
    part_of_speech = models.CharField(
        max_length=100, null=True, blank=True)  # Часть речи
    gender = models.CharField(max_length=10, null=True, blank=True)  # Род
    frequency = models.IntegerField(
        null=True, blank=True)  # Частота использования

    def __str__(self):
        return self.text


class Meaning(models.Model):
    word = models.ForeignKey(
        Word, on_delete=models.CASCADE, related_name='meanings')
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text


class Dictionary(models.Model):
    user = models.ForeignKey("user.User", related_name='words',
                             on_delete=models.CASCADE, blank=False, null=False)
    word = models.ForeignKey("word.Word", related_name='dictionary',
                             on_delete=models.CASCADE, blank=False, null=False)
    translation = cast(Translation, models.ForeignKey("word.Translation", related_name='users',
                                    on_delete=models.CASCADE, blank=False, null=False))

    date_added = models.DateTimeField(auto_now_add=True)
    
    training: "Training"
    
    objects: DictionaryCustomManager = DictionaryCustomManager()
    
    

    class Meta:
        unique_together = ('user', 'word', 'translation',)

    def __str__(self) -> str:
        return f"User: {self.user} add {self.word} - {self.translation}"


class Training(models.Model):
    dictionary = models.ForeignKey("word.Dictionary", related_name='training',
                                   on_delete=models.CASCADE, blank=False, null=False)

    type = models.ForeignKey("word.TrainingType", related_name='training',
                             on_delete=models.DO_NOTHING, blank=False, null=False)

    lvl = models.IntegerField("lvl", default=1, null=False)
    time = models.IntegerField("time", null=False)


    def __str__(self) -> str:
        return f"To {self.dictionary} add training {self.type}"


class TrainingType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"Training type: {self.name}"





