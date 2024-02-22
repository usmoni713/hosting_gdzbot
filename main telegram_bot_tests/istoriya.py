import requests
from bs4 import BeautifulSoup


def install_jpg(url: str) -> str:
    response = requests.get(url)
    name = (url.split("/"))[-1]
    with open(name, "wb") as file:
        file.write(response.content)
    # return name


def main():
    url = "https://гдз.рф/po-istorii/8-klass/arsentev#task?t=1-part-56"

    req = requests.get(url)
    src = str(req.text)
    # with open("file.html") as f:??
    soup = BeautifulSoup(src, "lxml")
    gdz_ls = (
        BeautifulSoup(
            str(
                soup.find("body")
                .find("div", {"id": "__nuxt"})
                .find("div", id="__layout")
                .find("div", {"class": "root", "data-v-491ebcd3": ""})
                .find("div", {"class": "page", "data-v-491ebcd3": ""})
                .find("div", {"class": "content", "data-v-491ebcd3": ""})
                .find("main", {"class": "book", "data-v-fc23600c": ""})
                .find("section", {"class": "task", "data-v-fc23600c": ""})
                .find("div")  # {"data-v-76d66542": "", "data-v-fc23600c": ""}
                .find("div", {"data-v-76d66542": "", "class": "solution"})
                .find_all(
                    "figure",
                    {
                        "data-v-7641e59f": "",
                        "data-v-76d66542": "",
                        "class": "edition",
                    },
                )[-1]
            ),
            "lxml",
        )
        .find("div", {"data-v-7641e59f": "", "class": "task-images"})
        .find_all("img", {"data-v-4df8d45c": "", "data-v-7641e59f": ""})
    )

    for el in gdz_ls:
        gdz = BeautifulSoup(str(el), "lxml")
        # print(gdz)
        install_jpg(str(gdz.find("img").get("src")))


if __name__ == "__main__":
    main()
