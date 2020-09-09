from bs4 import BeautifulSoup


def create_soup(page_content):
    return BeautifulSoup(page_content, "html.parser")


def search_in_soup(soup, pattern):
    return soup.findAll(**pattern)
