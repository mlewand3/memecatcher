import os

from flask import Flask, render_template, request, session
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect

from .src.scrap_page import scrap_pages

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(os.environ.get("APP_CONFIG"))

all_pages = ["JBZD", "kwejk", "faktopedia", "demotywatory"]


@app.route("/", methods=["GET", "POST"])
def meme_page():
    if request.method == "GET":
        if "checkpoints" not in session:
            session["checkpoints"] = {}

        memes, checkpoints = scrap_pages(
            pages=session.get("pages", ["JBZD", "kwejk"]),
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
            pages=session.get("pages", ["JBZD", "kwejk"]),
            all_pages=all_pages,
        )
    else:
        session["checkpoints"] = {request.form.keys()}
        return redirect("/")


if __name__ == "__main__":
    app.run()
