import os
import requests
from bs4 import BeautifulSoup
from sqlalchemy.exc import IntegrityError

from core.config import BaseConfig
from core.ext import db
from apps.portal.models import PortalModel

url: str = "https://sport.detik.com/indeks"

headers: dict = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
}


def get_all_items(url: str) -> list:

    res = requests.get(url, headers=headers)
    try:
        os.mkdir(os.path.join(BaseConfig.BASE_DIR, "temp"))
    except FileExistsError:
        pass

    # scrap temporary file untuk cek hasil scraping
    with open(
        os.path.join(os.path.join(BaseConfig.BASE_DIR, "temp"), "res.html"), "w"
    ) as f:
        f.write(res.text)
        f.close()

    # scraping step
    soup: BeautifulSoup = BeautifulSoup(res.text, "html.parser")

    # headers content
    contents = soup.find(
        "div", attrs={"class": "grid-row list-content", "id": "indeks-container"}
    ).find_all("article", attrs={"class": "list-content__item"})

    # process data
    results: list = []
    for content in contents:
        title = (
            content.find("h3", attrs={"class": "media__title"}).find("a").text.strip()
        )
        link = content.find("h3", attrs={"class": "media__title"}).find("a")["href"]
        date = content.find("div", attrs={"class": "media__date"}).find("span")["title"]
        images = (
            content.find("div", attrs={"class": "media__image"})
            .find("span")
            .find("img")["src"]
        )

        # mapping
        print("Process data: {}".format(title))
        data_dict: dict = {
            "title": title,
            "link": link,
            "date": date,
            "images": images,
        }
        results.append(data_dict)

    return results


def get_data(url: str):
    results: list = get_all_items(url)
    for result in results:
        print("save data: {}".format(result["title"], result["link"]))
        datas = PortalModel(
            title=result["title"],
            link=result["link"],
            date=result["date"],
            images=result["images"],
        )
        try:
            db.session.add(datas)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
