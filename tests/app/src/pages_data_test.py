"""
Those text exist only for checking if pages data arecomplete, and every site id described well
enough to be scrapped.
"""
import pytest
from app.src.pages_data import pages_data
from tests.util import get_all_pages_available

_LEGAL_EXTENSIONS = ("pl", "com", "org")


@pytest.mark.parametrize("page_name", get_all_pages_available())
def test_all_pages_has_valid_url_provided(page_name):
    # GIVEN
    page_data = pages_data[page_name]

    # WHEN
    url = page_data["url"]

    # THEN
    assert url.startswith("http")
    assert any([extension in url for extension in _LEGAL_EXTENSIONS])


@pytest.mark.parametrize("page_name", get_all_pages_available())
def test_all_pages_has_valid_img_pattern(page_name):
    # GIVEN
    page_data = pages_data[page_name]

    # WHEN
    img_pattern = page_data["img_pattern"]

    # THEN
    assert isinstance(img_pattern, dict)
    assert "name" in img_pattern.keys()


@pytest.mark.parametrize("page_name", get_all_pages_available())
def test_all_pages_has_valid_img_tag(page_name):
    # GIVEN
    page_data = pages_data[page_name]

    # WHEN
    img_tag = page_data["img_tag"]

    # THEN
    assert isinstance(img_tag, str)
    assert len(img_tag) > 0


@pytest.mark.parametrize("page_name", get_all_pages_available())
def test_all_pages_has_valid_page_direction(page_name):
    # GIVEN
    page_data = pages_data[page_name]

    # WHEN
    page_direction = page_data["page_direction"]

    # THEN
    assert isinstance(page_direction, str)
    assert page_direction in ["decreasing", "increasing"]


@pytest.mark.parametrize("page_name", get_all_pages_available())
def test_pages_with_decreasing_page_direction_has_page_pattern_included(page_name):
    # GIVEN
    page_data = pages_data[page_name]

    # WHEN
    page_direction = page_data["page_direction"]

    # THEN
    if page_direction == "decreasing":
        page_pattern = page_data["page_pattern"]
        assert isinstance(page_pattern, dict)


@pytest.mark.parametrize("page_name", get_all_pages_available())
def test_all_pages_has_valid_page_prefix(page_name):
    # GIVEN
    page_data = pages_data[page_name]

    # WHEN
    page_prefix = page_data["page_prefix"]

    # THEN
    assert isinstance(page_prefix, str)
