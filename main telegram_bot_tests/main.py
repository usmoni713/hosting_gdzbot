import asyncio
from typing import Any, Literal

from aiogram import Bot, Dispatcher, F
from aiogram.filters import BaseFilter, invert_f
from aiogram.types import Message

import buttons_gdz
import config_for_gdz as cfg


token = "6516484967:AAHMdMf7PpJBT0RP8XmP1LN03jam3gFq4tE"
bot = Bot(token=token)
dp = Dispatcher()
chanal_id = "@kaif_gdz"


def reset():
    cfg.us_class = 0
    cfg.us_num_exer = 0
    cfg.us_obj = ""


check_sub_channal = lambda chat_member: "left" not in str(chat_member)


def append_request(r: str, us: str) -> None:
    with open("request_gdz", "a") as requests:
        requests.write(f"{r} --> {us}\n")


class Chek_text_in_full_obj(BaseFilter):
    async def __call__(self, message: Message) -> dict[str, str] | Literal[False]:
        if str(message.text) in list(cfg.dict_full_obj.keys()):
            cfg.us_obj = cfg.dict_full_obj[str(message.text)]["obj"]
            cfg.us_obj_key = str(message.text)
            return {"foll_mess": cfg.dict_full_obj[str(message.text)]["mes_inp"]}
        return False


class check_sub_filter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return check_sub_channal(
            await bot.get_chat_member(chat_id=chanal_id, user_id=message.from_user.id)
        )


class chek_text_and_send_answer(BaseFilter):
    async def __call__(self, message: Message) -> dict[str, list[str]] | Literal[False]:
        if cfg.us_obj:
            try:
                exer_or_parag_or_page = cfg.dict_full_obj[cfg.us_obj_key]["items_use"]
                cfg.us_num_exer = int(str(message.text))
                await message.answer(
                    f"{cfg.us_obj}\n{exer_or_parag_or_page}: {cfg.us_num_exer}\nидет загрузка пожалуйста подождите..."
                )
                answers = cfg.dict_full_obj[cfg.us_obj_key]["func_get_gdz"](
                    cfg.us_num_exer
                )
                return {"ans": answers, "type_ans": "list"}

            except AttributeError as e:
                append_request(f"{message.text} , {e}", message.from_user.full_name)
                return {
                    "ans": "Извините, но мы не смогли найти такое задание!",
                    "type_ans": "str",
                }
            except IndexError as e:
                append_request(f"{message.text} , {e}", message.from_user.full_name)
                return {
                    "ans": "Извините, но мы не смогли найти такое задание!",
                    "type_ans": "str",
                }
            except ValueError as e:
                append_request(f"{message.text} , {e}", message.from_user.full_name)
                return {
                    "ans": "Извините. Можете ли вы уточнить, что вы имели в виду?",
                    "type_ans": "str",
                }


@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer(
        "Добро пожаловать!\nвыберите предмет:",
        reply_markup=buttons_gdz.choice_obj,
    )
    reset()


@dp.message(F.text == "/chek")
async def chek(message: Message):
    if not check_sub_channal(
        await bot.get_chat_member(chat_id=chanal_id, user_id=message.from_user.id)
    ):
        await message.answer(
            "чтобы пользоваться ботом необходимо подписаться на канал!!\n/chek\n",
            reply_markup=buttons_gdz.btn_subscribe,
        )
    else:
        reset()
        await message.answer(
            "\nвыберите предмет:\n",
            reply_markup=buttons_gdz.choice_obj,
        )


@dp.message(F.text == "/support")
async def start01(message: Message):
    await message.answer(
        "если у вас возникли какие то проблемы или вопросы пожалуйста напишите нам\nhttps://t.me/Usmoni03"
    )
    reset()


@dp.message(F.text == "/info")
async def start02(message: Message):
    reset()
    await message.answer(cfg.info_bot, reply_markup=buttons_gdz.choice_obj)


@dp.message(invert_f(check_sub_filter()))
async def start01(message: Message):
    await message.answer(
        "чтобы пользоваться ботом необходимо подписаться на канал!!\n/chek\n",
        reply_markup=buttons_gdz.btn_subscribe,
    )
    reset()


@dp.message(Chek_text_in_full_obj())
async def ans_choice_num_exer(message: Message, foll_mess: str):
    await message.answer(
        f"{foll_mess}",
        reply_markup=buttons_gdz.choice_num_exer,
    )


@dp.message(chek_text_and_send_answer())
async def ans_gdz(message: Message, ans: list | str, type_ans: str):
    if type_ans == "list":
        answers = ans
        for i in answers:
            await message.answer_document(str(i))
    elif type_ans == "str":
        await message.answer(text=ans)
    cfg.us_obj = ""
    await message.answer(
        "\nвыберите предмет:",
        reply_markup=buttons_gdz.choice_obj,
    )


@dp.message()
async def if_not_sub(message: Message):
    if not check_sub_channal(
        await bot.get_chat_member(chat_id=chanal_id, user_id=message.from_user.id)
    ):
        await message.answer(
            "чтобы пользоваться ботом необходимо подписаться на канал!!\n/chek\n",
            reply_markup=buttons_gdz.btn_subscribe,
        )


async def main_():
    await dp.start_polling(bot)


asyncio.run(main_())
