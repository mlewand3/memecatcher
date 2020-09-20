import pytest
from app.src.pages_data import pages_data
from app.src.pages_scrapper import PagesScrapper
from tests.util import get_all_pages_available

_EXTESNIONS = ["jpg", "png", "gif", "webm"]


def test_page_scraper_scrap_memes_for_all_sites_alvailable():
    # GIVEN
    pages_scrapper = PagesScrapper()

    # WHEN
    memes = pages_scrapper.scrap_pages(pages_names=get_all_pages_available(), page_number=1)

    # THEN
    assert len(memes) > 0

    for meme in memes:
        assert any([extension in meme for extension in _EXTESNIONS])


@pytest.mark.parametrize("page_number", list(range(10)))
def test_get_pages_urls_works_properly(page_number):
    # GIVEN
    pages_scrapper = PagesScrapper()

    # WHEN
    pages_urls = pages_scrapper._get_pages_urls(
        pages_names=get_all_pages_available(), page_number=page_number
    )

    # THEN
    assert len(pages_urls) > 0
    assert len(pages_urls) == len(get_all_pages_available())

    for url in pages_urls:
        assert "www" in url or "http" in url


@pytest.mark.parametrize("page_number", list(range(5)))
@pytest.mark.parametrize("page_name", get_all_pages_available())
def test_test_get_page_url_works_properly(page_name, page_number):
    # GIVEN
    pages_scrapper = PagesScrapper()

    # WHEN
    page_url = pages_scrapper._get_page_url(page_name=page_name, page_number=page_number)

    # THEN
    assert "www" in page_url or "http" in page_url
    if pages_data[page_name]["page_direction"] == "increasing":
        assert get_page_number_from_url(page_url) == str(page_number)

    elif pages_data[page_name]["page_direction"] == "decreasing":
        assert get_page_number_from_url(page_url) != str(page_number)


def get_page_number_from_url(url: str) -> int:
    """
    Yuck! Apparently some pages uses "," as a delimeter for page number, this function allows
    to retrieve that number despite strange ideas of some developers
    """
    last_token = url.split("/")[-1]
    return last_token.split(",")[-1]
