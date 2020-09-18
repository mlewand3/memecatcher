from bs4 import BeautifulSoup


def create_soup(page_content):
    """Creates BeautifulSoup object."""

    return BeautifulSoup(page_content, "html.parser")


def search_in_soup(soup: BeautifulSoup, pattern: dict):
    """ Search for specific pattern in BeautifulSoup object."""

    return soup.findAll(**pattern)
