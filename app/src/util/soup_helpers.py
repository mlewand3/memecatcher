import bs4


def create_soup(page_content: str) -> bs4.BeautifulSoup:
    """Creates BeautifulSoup object.

    Attrs:
        page_content - byte object represeinting site GET response.

    Returns:
        BeautifulSoup object representing page content.
    """

    return bs4.BeautifulSoup(page_content, "html.parser")


def search_in_soup(soup: bs4.BeautifulSoup, pattern: dict) -> bs4.element.ResultSet:
    """Search for specific pattern in BeautifulSoup object.

    Attrs:
        soup - BeautifulSoup object representing page content
        pattern - dict with pattern to be found in soup.

    Returns:
        bs4.element.ResultSet object
    """

    return soup.findAll(**pattern)
