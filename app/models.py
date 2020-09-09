from flask_user import UserMixin

from app.app import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default="")
    active = db.Column(db.Boolean(), nullable=False, server_default="0")

    pages = db.relationship("Page", secondary="user_pages")

    def __repr__(self):
        return f"{self.username}"

    @property
    def all_pages(self):
        return [page.name for page in self.pages]


class Page(db.Model):
    __tablename__ = "pages"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f"{self.name}"


class UserPages(db.Model):
    __tablename__ = "user_pages"

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id", ondelete="CASCADE"))
    page_id = db.Column(db.Integer(), db.ForeignKey("pages.id", ondelete="CASCADE"))
