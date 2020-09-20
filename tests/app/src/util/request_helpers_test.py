import pytest
from app.src.pages_data import pages_data
from app.src.util import get_url_content
from tests.util import get_all_pages_available


@pytest.mark.parametrize("page_name", get_all_pages_available())
def test_get_url_content_work_for_all_of_sites(page_name):
    # GIVEN
    url = pages_data[page_name]["url"]

    # WHEN
    content = get_url_content(url)

    # THEN
    assert content


@pytest.mark.parametrize("page_name", get_all_pages_available())
def test_get_url_content_work_for_all_of_sites_with_added_page_number(page_name):
    # GIVEN
    page_prefix = pages_data[page_name]["page_prefix"]
    sample_page_number = "5000"
    url = pages_data[page_name]["url"]
    url_with_page_number = url + page_prefix + sample_page_number

    # WHEN
    content = get_url_content(url_with_page_number)

    # THEN
    assert content
