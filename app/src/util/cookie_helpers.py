import json

from flask import request


def get_pages_to_show_from_cookies():
    cookie = request.cookies.get("pages")

    if not cookie:
        return ["JBZD", "kwejk"]
    else:
        return json.loads(cookie)
