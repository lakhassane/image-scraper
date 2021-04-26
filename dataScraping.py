from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil


url = 'http://www.jagodibuja.com/webcomic-living-with-hipstergirl-and-gamergirl-english/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

items = soup.find_all('figure', class_="gallery-item")
# items = soup.find_all('img', class_='attachment-thumbnail')

image_info = []
link_info = []

for i in items:
    image_tag = i.findChildren("a")
    # print(image_tag)
    link_info.append(image_tag[0]['href'])

# print(link_info)


def download_img(img):
    response = requests.get(img).content
    with open("images/" + str(i) + ".jpg", "wb") as f:
        f.write(response)
        print('Image scraped successfully.')


for i in range(0, len(link_info)):
    # print(link_info[i])
    response = requests.get(link_info[i])
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('img', class_="attachment-large")
    for j in items:
        download_img(j['src'])
        # image_info.append(j['src'])
        # print(image_info)


# for i in range(0, len(image_info)):
#     download_img(image_info[i])
