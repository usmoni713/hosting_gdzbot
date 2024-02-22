import requests
from bs4 import BeautifulSoup
import re


def install_jpg(url: str) -> str:
    response = requests.get(url)
    name = (url.split("/"))[-1]
    with open(name, "wb") as file:
        file.write(response.content)
    # return name


def get_num_tests(us_parag: int, head: str):
    url = f"https://otvetkin.info/reshebniki/8-klass/himiya/rudzitis"
    req = requests.get(url, headers=head)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    item_str = str(soup.find(string=re.compile(f"§ {us_parag}")).find_parent("div"))
    # item = BeautifulSoup(item_str, "lxml")
    it = re.findall(r"Тест №\d, Параграф", item_str)

    # num_items = item.find("div", class_="list-numbers").find_all("a", {"class":"link", "":"Вопрос №\d, Параграф 1"})
    return len(it)


def get_num_q(us_parag: int, head: str):
    url = f"https://otvetkin.info/reshebniki/8-klass/himiya/rudzitis"
    req = requests.get(url, headers=head)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    item_str = str(soup.find(string=re.compile(f"§ {us_parag}")).find_parent("div"))
    # item = BeautifulSoup(item_str, "lxml")
    it = re.findall(r"Вопрос №\d, Параграф", item_str)

    # num_items = item.find("div", class_="list-numbers").find_all("a", {"class":"link", "":"Вопрос №\d, Параграф 1"})
    return len(it)


def solo_q(us_parag: int, num_q: int):
    head = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.2470 Safari/537.36",
    }
    url = f"https://otvetkin.info/reshebniki/8-klass/himiya/rudzitis/vopros-{num_q}-paragraf-{us_parag}"
    req = requests.get(url, headers=head)
    soup = BeautifulSoup(req.text, "lxml")
    gdz = soup.find_all("img", class_="collapse-content__img img-responsive")
    ls_gdz_jpg = []
    for i in gdz:
        j = BeautifulSoup(str(i), "lxml").find("img")
        ls_gdz_jpg.append(f'https://otvetkin.info{j.get("src")}')
    return ls_gdz_jpg


def solo_test(us_parag: int, num_test: int):
    head = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.2470 Safari/537.36",
    }
    url = f"https://otvetkin.info/reshebniki/8-klass/himiya/rudzitis/test-{num_test}-paragraf-{us_parag}"
    req = requests.get(url, headers=head)
    soup = BeautifulSoup(req.text, "lxml")
    gdz = soup.find_all("img", class_="collapse-content__img img-responsive")
    ls_gdz_jpg = []
    for i in gdz:
        j = BeautifulSoup(str(i), "lxml").find("img")
        ls_gdz_jpg.append(f'https://otvetkin.info{j.get("src")}')
    return ls_gdz_jpg


def main(us_parag: int, us_obj="himiya"):
    head = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.2470 Safari/537.36",
    }
    num_q = get_num_q(us_parag, head)
    # print(num_q)
    num_tests = get_num_tests(us_parag, head)
    # print(num_tests)
    ls_gdz_q = []
    for i in range(1, num_q + 1):
        ls_gdz_q.append(solo_q(us_parag, i))
    ls_gdz_tests = []
    for i in range(1, num_tests + 1):
        ls_gdz_tests.append(solo_test(us_parag, i))
    gdz = []
    # print(ls_gdz_tests, ls_gdz_q)
    for i in ls_gdz_q:
        for j in i:
            gdz.append(f"{j}")
    for i in ls_gdz_tests:
        for j in i:
            gdz.append(j)
    return gdz


if __name__ == "__main__":
    a = main(us_parag=int(input("вводите номер упражнений:")))
    print(a)
