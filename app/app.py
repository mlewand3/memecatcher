import json
import os

from flask import Flask, make_response, render_template, request, send_from_directory
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect

from .src import PagesScrapper, get_pages_to_show_from_cookies

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(os.environ.get("APP_CONFIG"))
pages_scrapper = PagesScrapper()


@app.route("/")
@app.route("/<int:page_number>")
def meme_page(page_number: int = 1):
    pages = get_pages_to_show_from_cookies()

    memes = pages_scrapper.scrap_pages(pages, page_number)

    return render_template(
        template_name_or_list="meme_page.html",
        title="Meme Catcher",
        memes=memes,
        page_number=page_number,
    )


@app.route("/options", methods=["GET", "POST"])
def options():
    if request.method == "GET":
        return render_template(
            template_name_or_list="options.html",
            title="Options",
            pages=get_pages_to_show_from_cookies(),
            all_pages=pages_scrapper.get_all_pages_available,
        )
    else:
        response = make_response(redirect("/"))
        pages = json.dumps(list(request.form.keys()))
        response.set_cookie("pages", pages)

        return response


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run()
