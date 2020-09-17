from typing import List

from .pages_data import pages_data
from .util import (add_next_page_prefix, add_src_prefix, create_soup,
                   extract_tag_content, find_in_results, get_url_content,
                   search_in_soup, shuffle_lists)


def scrap_pages(pages: List[str], checkpoints: List[dict]):
    images = []
    new_checkpoints = {}

    for page in pages:
        url = checkpoints[page]
        new_images, new_checkpoint = scrap_page(page=page, url=url)

        new_checkpoints[page] = new_checkpoint
        images.append(new_images)

    shuffled_images = shuffle_lists(images)

    return shuffled_images, new_checkpoints


def scrap_page(page: str, url: str):
    page_content = get_url_content(url=url)
    soup = create_soup(page_content=page_content)

    images = find_images(soup, page)
    checkpoint = find_checkpoint(soup, page)

    return images, checkpoint


def find_images(soup, page: str):
    """ Find images in soup and adding src prefix if needed."""

    search_result = search_in_soup(soup=soup, pattern=pages_data[page]["img_pattern"])
    images = find_in_results(results=search_result, tag_to_find=pages_data[page]["img_tag"])
    images_with_prefix = add_src_prefix(images, pages_data[page].get("img_prefix"))

    return images_with_prefix


def find_checkpoint(soup, page):
    """Find anchro tag which directs to next page of memes in scrapped page."""

    next_page_data = search_in_soup(soup=soup, pattern=pages_data[page]["page_pattern"])
    checkpoint = extract_tag_content(result=next_page_data, tag="href")
    checkpoint_with_prefix = add_next_page_prefix(checkpoint, pages_data[page].get("page_prefix"))

    return checkpoint_with_prefix
