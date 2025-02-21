import base64
from random import randint


def clean_password(password):
    password = base64.b64decode(password)
    return str(password, 'utf-8')


def happy_birthday_message(make_txt):
    dict_birthday = make_txt.read_data("dictionary/happy_birthday")
    random_array_number = randint(0, len(dict_birthday) - 1)
    return dict_birthday[random_array_number]


def string_to_array(text_string):
    return text_string.split(", ")
