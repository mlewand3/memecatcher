import os

from flask import Flask, render_template, request, session
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_user import (UserManager, current_user, login_required,
                        user_logged_in, user_logged_out, user_registered)
from werkzeug.utils import redirect

from .src.scrap_page import scrap_pages

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(os.environ.get("APP_CONFIG"))
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.models import Page, User

user_manager = UserManager(app, db, User)


@user_logged_in.connect_via(app)
def _after_login_hook(sender, user, **extra):
    session["checkpoints"] = {}


@user_logged_out.connect_via(app)
def _after_logout_hook(sender, user, **extra):
    session["checkpoints"] = {}


@user_registered.connect_via(app)
def _after_user_registered_hook(sender, user, **extra):
    jbzd_page = Page.query.filter_by(name="JBZD").first()
    kwejk_page = Page.query.filter_by(name="kwejk").first()
    faktopedia = Page.query.filter_by(name="faktopedia").first()
    demotywatory = Page.query.filter_by(name="demotywatory").first()

    if not jbzd_page:
        jbzd_page = Page(name="JBZD")

    if not kwejk_page:
        kwejk_page = Page(name="kwejk")

    if not faktopedia:
        faktopedia = Page(name="faktopedia")

    if not demotywatory:
        demotywatory = Page(name="demotywatory")

    db.session.add(jbzd_page)
    db.session.add(kwejk_page)
    db.session.add(faktopedia)
    db.session.add(demotywatory)

    user.pages.append(jbzd_page)
    user.pages.append(kwejk_page)
    user.pages.append(faktopedia)
    user.pages.append(demotywatory)

    db.session.commit()


@app.route("/", methods=["GET", "POST"])
@login_required
def meme_page():
    if request.method == "GET":
        if "checkpoints" not in session:
            session["checkpoints"] = {}

        memes, checkpoints = scrap_pages(
            pages=current_user.pages,
            checkpoints=session.get("checkpoints"),
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
@login_required
def profile():
    if request.method == "GET":
        return render_template(
            template_name_or_list="profile.html",
            title="Profle",
            user_data=current_user,
            pages=db.session.query(Page),
        )
    else:
        pages = db.session.query(Page)

        for page in pages:
            page_in_db = page.name in current_user.all_pages
            page_in_form = page.name in request.form.keys()

            if page_in_form and not page_in_db:
                current_user.pages.append(page)
                db.session.commit()

            elif not page_in_form and page_in_db:
                current_user.pages.remove(page)
                db.session.commit()

            else:
                continue

        session["checkpoints"] = {}

        return redirect("/")


if __name__ == "__main__":
    app.run()
