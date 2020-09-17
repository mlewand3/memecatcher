import requests


def get_url_content(url: str):
    """ Get url content."""

    return requests.get(url).content
