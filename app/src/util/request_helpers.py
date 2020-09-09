import requests


def get_url_content(url: str):
    return requests.get(url).content
