from typing import List

from .pages_data import pages_data
from .util import (add_src_prefix, create_soup, find_in_results,
                   get_url_content, search_in_soup, shuffle_lists)


def scrap_pages(pages: List[str], urls: List[dict]):
    images = []

    for page, url in zip(pages, urls):
        new_images = scrap_page(page=page, url=url)
        images.append(new_images)

    shuffled_images = shuffle_lists(images)

    return shuffled_images


def scrap_page(page: str, url: str):
    page_content = get_url_content(url=url)
    soup = create_soup(page_content=page_content)

    images = find_images(soup, page)

    return images


def find_images(soup, page: str):
    """ Find images in soup and adding src prefix if needed."""

    search_result = search_in_soup(soup=soup, pattern=pages_data[page]["img_pattern"])
    images = find_in_results(results=search_result, tag_to_find=pages_data[page]["img_tag"])
    images_with_prefix = add_src_prefix(images, pages_data[page].get("img_prefix"))

    return images_with_prefix


def get_pages_urls(pages: List[str], page_number: int) -> List[str]:
    urls = []

    for page in pages:
        if pages_data[page]["page_direction"] == "increasing":
            url = pages_data[page]["url"] + pages_data[page]["page_prefix"] + str(page_number)
            urls.append(url)

        elif pages_data[page]["page_direction"] == "decreasing":

            if not pages_data[page].get("start_from"):
                pages_data[page]["start_from"] = find_starting_page(page)

            number = pages_data[page]["start_from"] - page_number
            url = pages_data[page]["url"] + pages_data[page]["page_prefix"] + str(number)

            urls.append(url)

    return urls


def find_starting_page(page: dict) -> int:
    page_content = get_url_content(url=pages_data[page]["url"])
    soup = create_soup(page_content=page_content)
    results = search_in_soup(soup, pages_data[page]["page_pattern"])

    number = extract_page_number(results)

    return number


def extract_page_number(results) -> int:
    for result in results[0]:
        try:
            number = result.text
        except AttributeError:
            pass

    return int(number)
