import requests
from bs4 import BeautifulSoup


def install_jpg(url: str) -> str:
    response = requests.get(url)
    name = f'{(url.split("/"))[-2:-1]}'
    with open(name, "wb") as file:
        file.write(response.content)


def solo_exer(us_exer: int, us_obj="fizika") -> list:
    head = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.2470 Safari/537.36",
    }
    url = f"https://gdz.red/8-klass/8-{us_obj}/fizika-8-klass-uchebnik-peryshkin/8-perishkin-uchebnik-upr-{us_exer}.html"

    req = requests.get(url, headers=head)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    img_s = (
        soup.find("div", {"class": "entry-content", "itemprop": "articleBody"})
    ).find_all(
        "img",
        {
            "decoding": "async",
        },
    )
    ls_url_img = []
    for i in img_s:
        form = (f'https://gdz.red{i.get("src")}'.split("/"))[-1][-3::1]
        if form == "jpg":
            ls_url_img.append(f'https://gdz.red{i.get("src")}')

    return ls_url_img


def solo_task(
    us_parag: int,
) -> list:
    head = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.2470 Safari/537.36",
    }
    url = f"https://gdz.red/8-klass/8-fizika/fizika-8-klass-uchebnik-peryshkin/8-perishkin-uchebnik-par-{us_parag}.html"
    req = requests.get(url, headers=head)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    img_s = (
        soup.find("div", {"class": "entry-content", "itemprop": "articleBody"})
    ).find_all(
        "img",
        {
            "decoding": "async",
        },
    )
    ls_url_img = []
    for i in img_s:
        form = (f'https://gdz.red{i.get("src")}'.split("/"))[-1][-3::1]
        if form == "jpg":
            ls_url_img.append(f'https://gdz.red{i.get("src")}')

    return ls_url_img


def main(us_parag: int, us_obj="fizika"):
    url = f"https://gdz.red/8-klass/8-{us_obj}/fizika-8-klass-uchebnik-peryshkin/8-perishkin-uchebnik-voprosi-{us_parag}.html"
    head = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.2470 Safari/537.36",
    }
    req = requests.get(url, headers=head)
    src = req.text
    soup = BeautifulSoup(src, "lxml")

    img_s = (
        soup.find("div", {"class": "entry-content", "itemprop": "articleBody"})
    ).find_all(
        "img",
        {
            "decoding": "async",
        },
    )
    ls_url_img = []
    for i in img_s:
        form = (f'https://gdz.red{i.get("src")}'.split("/"))[-1][-3::1]
        if form == "jpg":
            ls_url_img.append(f'https://gdz.red{i.get("src")}')

    url_main = f"https://gdz.red/8-klass/8-fizika/fizika-8-klass-uchebnik-peryshkin"
    req_main = requests.get(url_main, headers=head)
    src_main = req_main.text
    soup_main = BeautifulSoup(src_main, "lxml")
    task = soup_main.find(string="Задания параграфов").find_next("div")
    if str(
        f"/8-klass/8-fizika/fizika-8-klass-uchebnik-peryshkin/8-perishkin-uchebnik-par-{us_parag}.html"
    ) in str(task):
        gdz_task = solo_task(us_parag, head)
        for i in gdz_task:
            ls_url_img.append(str(i))
    return ls_url_img


if __name__ == "__main__":
    main(us_parag=int(input("вводите номер параграф:")))
