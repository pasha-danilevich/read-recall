from django.conf import settings as django_settings
import os
import json
from random import randint, choice

from apps.word.utils import get_current_unix_time


def _get_time_on_lvl(levels, current_lvl: int) -> int:
    second_in_day = 86400
    try:
        day_in_lvl = levels[current_lvl-1]
    except IndexError:  # если индекс больше или меньше существуещего, то ставим последнюю дату
        day_in_lvl = levels[-1]

    time = second_in_day * day_in_lvl
    return time


def _is_last_level(levels, current_lvl: int):
    count_lvl = len(levels)

    if count_lvl <= current_lvl:
        return True

    return False


def _is_first_level(current_lvl: int):
    if current_lvl == 1:
        return True
    return False

def get_new_lvl(is_correct, levels, current_lvl) -> int:
    if is_correct:
        if not _is_last_level(levels, current_lvl):
            new_lvl = current_lvl + 1
        else:
            # остается на прежднем уровне (1й или последний)
            new_lvl = current_lvl
            
    else:
        if not _is_first_level(current_lvl):
            new_lvl = current_lvl - 1
        else:
            # остается на прежднем уровне (1й или последний)
            new_lvl = current_lvl

    return new_lvl

def get_new_time(levels, new_lvl):
    return get_current_unix_time() + _get_time_on_lvl(levels, new_lvl)

class StaticFileContextManager:
    def __init__(self, filename, mode='r'):
        self.file_path = os.path.join(django_settings.STATIC_ROOT, filename)
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_path, self.mode, encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


def get_false_set(instance, part_of_speech: str, number_of_false_set: int):

    file_names = ['FalseSet.json', 'FalseSet_2.json']
    file_name = file_names[randint(0, 1)]

    with StaticFileContextManager(file_name) as file:
        data_dict = json.loads(file.read())
        part_of_speech = _convert_part_of_speech(part_of_speech)
        target_words_on_part = data_dict.get(part_of_speech)

        return _generate_false_set(instance, target_words_on_part, number_of_false_set)


def _convert_part_of_speech(part_of_speech: str):
    part_set = {
        'глагол': 'vb',
        'причастие': 'prt',  # в разработке
        'существительное': 'nn',
        'наречие': 'adv',
        'прилагательное': 'adj',
        'mix': 'mix'
    }
    part_of_speech = part_set.get(part_of_speech, 'mix')

    return part_of_speech


def _generate_false_set(instance, word_list, number_of_false_set):
    false_set = []
    for _ in range(number_of_false_set):

        word = choice(word_list)
        text = word['val']

        if text == instance.text:
            continue

        translation = choice(word['tr'])

        false_word = {
            "text": text,
            "translation": translation
        }
        false_set.append(false_word)

    return _unique_dict_list(false_set)


def _unique_dict_list(dict_list):
    unique_dicts = []
    unique_translations = set()

    for d in dict_list:
        text = d['translation']
        if text not in unique_translations:
            unique_translations.add(text)
            unique_dicts.append(d)

    return unique_dicts
