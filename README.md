# image-scraper

Scraping images on the web

This is a quick script to scrape images on a website (`dataScraping.py`).

Tested on `http://www.jagodibuja.com/`.

One major lookout is the fact that in that website, you first get thumbnails (which are quite unreadable).

If you need the actual images, you need to scrape each picture's link, get to that link and scrape the image.

`shingeky.py` loops through multiple pages of a website to scrap images. Each pages is created as folder in the destination filesystem.
