import pytest
from app.src.pages_data import pages_data
from app.src.util import create_soup, get_url_content, search_in_soup
from tests.util import get_all_pages_available


@pytest.mark.parametrize("page_name", get_all_pages_available())
def test_create_soup_works_properly(page_name):
    # GIVEN
    content = get_url_content(url=pages_data[page_name]["url"])

    # WHEN
    soup = create_soup(content)

    # THEN
    assert soup


@pytest.mark.parametrize("page_name", get_all_pages_available())
def test_seach_in_soup_works_properly_for_all_patterns_used_for_images(page_name):
    # GIVEN
    content = get_url_content(url=pages_data[page_name]["url"])
    pattern = pages_data[page_name]["img_pattern"]

    # WHEN
    soup = create_soup(content)
    search_results = search_in_soup(soup, pattern)

    # THEN
    assert search_results


@pytest.mark.parametrize("page_name", get_all_pages_available())
def test_seach_in_soup_works_properly_for_all_patterns_used_for_paginations(page_name):
    # GIVEN
    content = get_url_content(url=pages_data[page_name]["url"])
    pattern = pages_data[page_name].get("page_pattern")

    # WHEN & THEN
    if not pattern:
        assert True
    else:
        soup = create_soup(content)
        assert search_in_soup(soup, pattern)
