import datetime
from app import db
from slugify import slugify


class Snippet(db.Model):
    STATUS_PUBLIC = 0
    STATUS_DRAFT = 1
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    slug = db.Column(db.String(100), unique=True)
    body = db.Column(db.Text)
    status = db.Column(db.SmallInteger, default=STATUS_PUBLIC)
    created_timestamp = db.Column(db.DateTime,
                                  default=datetime.datetime.now)
    modified_timestamp = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call
        self.generate_slug()

    def generate_slug(self):
        self.slug = ''
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Snippet: %s>' % self.title
