from FlaskProjectPackage import db


class News(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=60), nullable=False, unique=True)
    description = db.Column(db.String(length=8096), nullable=False, unique=True)
    category = db.Column(db.String(length=30), nullable=False)
    date = db.Column(db.String(length=30), nullable=False)
    author = db.Column(db.String(length=60), nullable=False)