import json
import os

from flask import Flask, make_response, render_template, request
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect

from .src import get_pages_urls, pages_data, scrap_pages
from .src.util import get_pages_to_show_from_cookies

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(os.environ.get("APP_CONFIG"))
all_pages = list(pages_data.keys())


@app.route("/")
@app.route("/<int:page_number>")
def meme_page(page_number: int = 1):
    pages = get_pages_to_show_from_cookies()
    pages_urls = get_pages_urls(pages, page_number)

    memes = scrap_pages(pages, pages_urls)

    return render_template(
        template_name_or_list="base.html",
        title="Meme Catcher",
        memes=memes,
        page_number=page_number,
    )


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "GET":
        return render_template(
            template_name_or_list="profile.html",
            title="Profle",
            pages=get_pages_to_show_from_cookies(),
            all_pages=all_pages,
        )
    else:
        response = make_response(redirect("/"))
        pages = json.dumps(list(request.form.keys()))
        response.set_cookie("pages", pages)

        return response


if __name__ == "__main__":
    app.run()
