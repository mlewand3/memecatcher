from itertools import chain, zip_longest
from typing import List

from .util import (create_soup, extract_tag_content, find_in_results,
                   get_url_content, search_in_soup)

pages_data = {
    "JBZD": {
        "url": "https://jbzd.com.pl/",
        "tags": ["alt", "src"],
        "img_pattern": {"name": "img", "attrs": {"class": "article-image"}},
        "page_pattern": {"name": "a", "attrs": {"class": "pagination-next"}},
    },
    "kwejk": {
        "url": "https://kwejk.pl/",
        "tags": ["alt", "src"],
        "img_pattern": {"name": "img", "attrs": {"class": "full-image"}},
        "page_pattern": {"name": "a", "attrs": {"class": "btn btn-next btn-gold"}},
    },
    "faktopedia": {
        "url": "https://faktopedia.pl/",
        "tags": ["alt", "src"],
        "img_prefix": "https://faktopedia.pl",
        "img_pattern": {"name": "img", "attrs": {"class": "pic"}},
        "page_pattern": {"name": "a", "attrs": {"class": "prefetch list_next_page_button"}},
    },
    "demotywatory": {
        "url": "https://demotywatory.pl/",
        "tags": ["alt", "src"],
        "img_pattern": {"name": "img", "attrs": {"class": "demot"}},
        "page_pattern": {"name": "a", "attrs": {"class": "prefetch list_next_page_button"}},
    },
}


def scrap_page(page: dict, checkpoint):
    page_data = pages_data[page]

    if not checkpoint:
        page_content = get_url_content(url=page_data["url"])
    else:
        page_content = get_url_content(url=checkpoint)

    soup = create_soup(page_content=page_content)
    search_result = search_in_soup(soup=soup, pattern=page_data["img_pattern"])

    next_page_data = search_in_soup(soup=soup, pattern=page_data["page_pattern"])
    checkpoint = extract_tag_content(result=next_page_data, tag="href")

    images = find_in_results(results=search_result, tags=page_data["tags"])

    if page_data.get("img_prefix"):
        prefix = page_data["img_prefix"]
        images = [{"alt": img["alt"], "src": prefix + img["src"]} for img in images]

    return images, checkpoint


def scrap_pages(pages: List[str], checkpoints):
    memes_lists = []

    for page in pages:
        meme_list, checkpoint = scrap_page(page.name, checkpoints.get(page.name))
        checkpoints[page.name] = checkpoint
        memes_lists.append(meme_list)

    shuffled_meme_list = _shuffle_lists(memes_lists)

    return shuffled_meme_list, checkpoints


def _shuffle_lists(_lists):
    result = []

    while any(_lists):
        for _list in _lists:
            if len(_list) == 0:
                pass
            else:
                result.append(_list.pop(0))

    return result
