import requests
from bs4 import BeautifulSoup


# def install_jpg(url: str) -> str:
#     response = requests.get(url)
#     name = f'{(url.split("/"))[-1]}.jpg'
#     with open(name, "wb") as file:
#         file.write(response.content)
#     # return name


def main(us_exers: int, us_obj="geometria"):
    url = f"https://gdz.today/za-7-class/{us_obj}/atanasyan-uchebnik/1-{us_exers}"
    head = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.2470 Safari/537.36",
    }
    req = requests.get(url, headers=head)
    src = req.text

    soup = BeautifulSoup(src, "lxml")

    overtask = soup.find("div", class_="task").find_all("div", class_="overtask")
    ls_url_img = []
    for i in overtask:
        j = BeautifulSoup(str(i), "lxml")
        ls_url_img.append(f'https://gdz.today{j.find("img").get("data-src")}')
    # install_jpg(ls_url_img[1])
    return ls_url_img


if __name__ == "__main__":
    a = main(us_exers=int(input("вводите номер упражнений:")))
    # print(a)
