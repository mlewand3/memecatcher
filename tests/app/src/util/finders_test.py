import pytest
from app.src.pages_data import pages_data
from app.src.util import (
    create_soup,
    find_page_number,
    find_tag_in_results,
    get_url_content,
    search_in_soup,
)
from tests.util import get_all_pages_available, get_all_pages_with_decreasing_page_number


@pytest.mark.parametrize("page_name", get_all_pages_available())
def test_find_tag_in_results_work_for_every_site_finding_memes(page_name):
    # GIVEN
    img_pattern = pages_data[page_name]["img_pattern"]
    img_tag = pages_data[page_name]["img_tag"]
    content = get_url_content(url=pages_data[page_name]["url"])
    soup = create_soup(content)
    find_results = search_in_soup(soup, img_pattern)

    # WHEN
    tag_found = find_tag_in_results(find_results, img_tag)

    # THEN
    assert len(tag_found) > 0


@pytest.mark.parametrize("page_name", get_all_pages_with_decreasing_page_number())
def test_find_page_number_works_properly(page_name):
    # GIVEN
    page_pattern = pages_data[page_name]["page_pattern"]
    content = get_url_content(url=pages_data[page_name]["url"])
    soup = create_soup(content)
    find_results = search_in_soup(soup, page_pattern)

    # WHEN
    tag_found = find_page_number(find_results)

    # THEN
    assert tag_found
    assert isinstance(tag_found, int)
