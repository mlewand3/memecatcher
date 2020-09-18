from bs4 import BeautifulSoup


def create_soup(page_content: str) -> BeautifulSoup:
    """Creates BeautifulSoup object.

    Attrs:
        page_content - byte object represeinting site GET response.

    Returns:
        BeautifulSoup object representing page content.
    """

    return BeautifulSoup(page_content, "html.parser")


def search_in_soup(soup: BeautifulSoup, pattern: dict):
    """Search for specific pattern in BeautifulSoup object.

    Attrs:
        soup - BeautifulSoup object representing page content
        pattern - dict with pattern to be found in soup.

    Returns:
        ???
    """

    return soup.findAll(**pattern)
