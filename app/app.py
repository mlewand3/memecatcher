import json
import os

from flask import Flask, make_response, render_template, request, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect

from .src import pages_data, scrap_pages
from .src.models import Checkpoints
from .src.util import get_pages_to_show_from_cookies

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(os.environ.get("APP_CONFIG"))
all_pages = list(pages_data.keys())

checkpoints = Checkpoints()


@app.route("/")
@app.route("/<int:page_number>")
def meme_page(page_number: int = 0):
    global checkpoints

    if checkpoints.is_empty:
        pages = get_pages_to_show_from_cookies()
        checkpoints[0] = {name: data["url"] for name, data in pages_data.items() if name in pages}

    if not checkpoints[page_number]:
        return redirect(url_for("meme_page"))

    memes, new_checkpoints = scrap_pages(
        pages=get_pages_to_show_from_cookies(),
        checkpoints=checkpoints[page_number],
    )

    checkpoints[page_number + 1] = new_checkpoints

    return render_template(
        template_name_or_list="base.html",
        title="Meme Catcher",
        memes=memes,
        page_number=page_number,
    )


@app.route("/profile", methods=["GET", "POST"])
def profile():
    global checkpoints

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
        print(pages)

        checkpoints[0] = {name: data["url"] for name, data in pages_data.items() if name in pages}

        return response


if __name__ == "__main__":
    app.run()
