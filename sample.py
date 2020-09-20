import pickle

from app.src import PagesScrapper
from app.src.util import get_url_content

page_scapper = PagesScrapper()
all_pages = page_scapper.get_all_pages_available


for page in all_pages:
    content = get_url_content(page_scapper.pages_data[page]["url"])
    with open("content_" + page, "wb") as file:
        pickle.dump(content, file)
