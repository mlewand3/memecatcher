import json
import os

from flask import (Flask, make_response, render_template, request, session,
                   url_for)
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect

from .src import pages_data, scrap_pages
from .src.util import get_pages_to_show_from_cookies

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(os.environ.get("APP_CONFIG"))

all_pages = list(pages_data.keys())


@app.route("/", methods=["GET", "POST"])
def meme_page():
    if request.method == "GET":
        if "checkpoints" not in session:
            session["checkpoints"] = {}

        memes, checkpoints = scrap_pages(
            pages=get_pages_to_show_from_cookies(),
            checkpoints=session.get("checkpoints", {}),
        )

        session["checkpoints"] = checkpoints

        return render_template(
            template_name_or_list="base.html",
            title="Meme Catcher",
            memes=memes,
        )
    else:
        session["checkpoints"] = {}
        return redirect("/")


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
        session["checkpoints"] = {}

        response = make_response(redirect("/"))
        response.set_cookie("pages", json.dumps(list(request.form.keys())))

        return response


if __name__ == "__main__":
    app.run()
