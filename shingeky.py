from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil
import re
import os


url = 'https://attaquetitans.com/manga/shingeki-no-kyojin-scan-'
page = 9
offset = 130


def download_img(img, i, page):
    print('img', img)
    response = requests.get(img).content
    with open(page + "/" + str(i) + ".jpg", "wb") as f:
        f.write(response)
        print("saving in", page)
        # print('Image scraped successfully.')


def execute(url, page):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    # items = soup.find_all("img", href=re.compile("s1600"))
    items = soup.find_all("img", attrs={"data-original-width": "1365"})

    print(items)

    if items:
        os.mkdir(page)

    for i in range(0, len(items)):
        # print(i)
        download_img(items[i]['src'], i, page)


def loop_chapters(url, ind):
    p = offset + ind
    url = url + "" + str(p)
    print('url', url)
    os.mkdir("SNK" + str(p))
    execute(url, "SNK" + str(p))


for j in range(0, 12):
    loop_chapters(url, j)
