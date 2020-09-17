import json

from flask import request


def get_pages_to_show_from_cookies():
    """Gets cookie to detrmine which pages will be shown to user."""

    cookie = request.cookies.get("pages")

    if not cookie:
        return ["JBZD", "kwejk"]
    else:
        return json.loads(cookie)
