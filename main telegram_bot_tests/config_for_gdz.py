import algebra
import anglijskij
import biologiya
import geografiya
import geometria
import himiya
import obshhestvoznanie
import russkii
import fizika

us_obj = ""
us_obj_key = ""
us_num_exer = 0
mes_inp_num_exer = "введите номер упражнение"
mes_inp_num_page = "введите номер Страницы"
# mes_inp_num_exer_f_russ = "вводите номер упражнение:"
mes_inp_num_parag = "введите номер параграф:"
# numbers = [i for i in range(99999]
user_name = ""
ls_obj_use_exer = ["russkii", "algebra", "geometria", "exer_fizika"]
ls_items_use_parag = ["himiya", "geografiya", "obshhestvoznanie", "biologiya", "fizika"]
ls_items_use_page = ["anglijskij"]
us_class = 0
class_selected = False

dict_full_obj = {
    "/русский язык": {
        "obj": "russkii",
        "mes_inp": mes_inp_num_exer,
        "items_use": "упражнение",
        "func_get_gdz": russkii.main,
    },
    "/алгебра": {
        "obj": "algebra",
        "mes_inp": mes_inp_num_exer,
        "items_use": "упражнение",
        "func_get_gdz": algebra.main,
    },
    "/геометрия": {
        "obj": "geometria",
        "mes_inp": mes_inp_num_exer,
        "items_use": "упражнение",
        "func_get_gdz": geometria.main,
    },
    "/химия": {
        "obj": "himiya",
        "mes_inp": mes_inp_num_parag,
        "items_use": "параграф",
        "func_get_gdz": himiya.main,
    },
    "/география": {
        "obj": "geografiya",
        "mes_inp": mes_inp_num_parag,
        "items_use": "параграф",
        "func_get_gdz": geografiya.main,
    },
    "/обществознание": {
        "obj": "obshhestvoznanie",
        "mes_inp": mes_inp_num_parag,
        "items_use": "параграф",
        "func_get_gdz": obshhestvoznanie.main,
    },
    "/биология": {
        "obj": "biologiya",
        "mes_inp": mes_inp_num_parag,
        "items_use": "параграф",
        "func_get_gdz": biologiya.main,
    },
    "/английский язык": {
        "obj": "anglijskij",
        "mes_inp": mes_inp_num_page,
        "items_use": "Страница",
        "func_get_gdz": anglijskij.main,
    },
    "/физика": {
        "obj": "fizika",
        "mes_inp": mes_inp_num_parag,
        "items_use": "параграф",
        "func_get_gdz": fizika.solo_task,
    },
    "/упражнения по физике": {
        "obj": "exer_fizika",
        "mes_inp": mes_inp_num_exer,
        "items_use": "упражнение",
        "func_get_gdz": fizika.solo_exer,
    },
}

ls_full_obj = [
    "/start",
    "/русский язык",
    "/алгебра",
    "/геометрия",
    "/химия",
    "/география",
    "/обществознание",
    "/биология",
    "/английский язык",
    "/упражнения по физике",
    "/физика",
]

info_bot = "Бот был создан для помощи пользователям в решении различных задач и вопросов. Он использует ресурсы из интернета для анализа запросов и предоставления ответов. Бот может помочь с выполнением различных задач, связанных с школьной программой. Бот постоянно обновляется и улучшается, чтобы быть более эффективным и полезным для пользователей.\nРазработчик: Усмони Кабир\n"
