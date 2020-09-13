from typing import List

from .pages_data import pages_data
from .util import (create_soup, extract_tag_content, find_in_results,
                   get_url_content, search_in_soup, shuffle_lists)


def scrap_pages(pages: List[str], checkpoints: List[dict]):
    memes_lists = []

    for page in pages:
        meme_list, checkpoint = scrap_page(page, checkpoints.get(page))
        checkpoints[page] = checkpoint
        memes_lists.append(meme_list)

    shuffled_meme_list = shuffle_lists(memes_lists)

    return shuffled_meme_list, checkpoints


def scrap_page(page: dict, checkpoint: dict):
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
