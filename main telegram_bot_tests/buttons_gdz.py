from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

ls_obj = [
    [KeyboardButton(text="/русский язык"), KeyboardButton(text="/алгебра")],
    [KeyboardButton(text="/геометрия"), KeyboardButton(text="/химия")],
    [KeyboardButton(text="/география"), KeyboardButton(text="/обществознание")],
    [KeyboardButton(text="/биология"), KeyboardButton(text="/английский язык")],
    [KeyboardButton(text="/физика"), KeyboardButton(text="/упражнения по физике")]
]
# fizika
ls_classes = [[], []]
n = 0
for i in range(1, 12):
    if i % 4 == 0:
        ls_classes.append([])
        n += 1
    ls_classes[n].append(KeyboardButton(text=f"{i}"))
choice_num_class = ReplyKeyboardMarkup(
    keyboard=ls_classes, resize_keyboard=True, input_field_placeholder="класс:"
)

choice_obj = ReplyKeyboardMarkup(
    keyboard=ls_obj,
    resize_keyboard=True,
    input_field_placeholder="выберите предмет:",
)
ls_exer = [[], []]
j = 0
for i in range(1, 400):
    if i % 8 == 0:
        ls_exer.append([])
        j += 1
    ls_exer[j].append(KeyboardButton(text=f"{i}"))
choice_num_exer = ReplyKeyboardMarkup(
    keyboard=ls_exer, resize_keyboard=True, input_field_placeholder="упражнение:"
)

ls_btn_subscribe = [
    [InlineKeyboardButton(text="ПОДПИСАТЬСЯ", url="https://t.me/kaif_gdz")],
    [],
]


btn_subscribe = InlineKeyboardMarkup(inline_keyboard=ls_btn_subscribe)
# btn_subscribe.add(ls_btn_subscribe)
ls_btn_check_subs = [[KeyboardButton(text="/chek")]]
btn_check_subs = ReplyKeyboardMarkup(keyboard=ls_btn_check_subs, resize_keyboard=True)
