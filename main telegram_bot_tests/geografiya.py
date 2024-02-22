import requests
from bs4 import BeautifulSoup


# def install_jpg(url: str) -> str:
#     response = requests.get(url)
#     name = (url.split("/"))[-1]
#     with open(name, "wb") as file:
#         file.write(response.content)
#     # return name


def main(us_parag: int, us_obj="geografiya"):
    url = f"https://gdz.red/8-klass/8-{us_obj}/geografiya-8-klass-uchebnik-alekseev-nikolina/8-geogafiya-uch-alekseev-nikolina-vopr-k-par-{us_parag}.html"
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
        # print(f'https:{i.get("data-img-src")}')
    # install_jpg(url_img)
    return ls_url_img


if __name__ == "__main__":
    a = main(us_parag=int(input("вводите номер параграф:")))
    print(a)
