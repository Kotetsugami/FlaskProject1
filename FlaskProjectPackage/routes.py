from FlaskProjectPackage import app
from flask import render_template, redirect, url_for, request, flash
from FlaskProjectPackage import db
from FlaskProjectPackage.models import News
from FlaskProjectPackage.forms import CreateNews, DeleteNews, ChangeNews, GetNews
import datetime
import sqlite3 as sql


def get_db_connection():
    conn = sql.connect('database.db')
    conn.row_factory = sql.Row
    return conn


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route("/create", methods=['GET', 'POST'])
def create_page():
    create_form = CreateNews()
    if create_form.validate_on_submit():
        new_user = News(title=create_form.title.data,
                        description=create_form.description.data,
                        category=create_form.category.data,
                        date=datetime.datetime.now(),
                        author=create_form.author.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home_page'))

    return render_template("create.html", form=create_form)


@app.route("/delete", methods=['GET', 'POST'])
def delete_page():
    delete_form = DeleteNews()
    if delete_form.validate_on_submit():
        news = News.query.filter_by(title=delete_form.title.data).first()
        if news:
            db.session.delete(news)
            db.session.commit()

    return render_template("delete.html", form=delete_form)


@app.route("/change", methods=['GET', 'POST'])
def change_page():
    change_form = ChangeNews()
    if change_form.validate_on_submit():
        news = News.query.filter_by(title=change_form.title.data).first()
        if news:
            news.description = change_form.description.data
            db.session.commit()

    return render_template("change.html", form=change_form)


@app.route("/get", methods=['GET', 'POST'])
def get_page():
    get_form = GetNews()
    if get_form.validate_on_submit():
        news = News.query.filter_by(title=get_form.title.data)
        return render_template("get.html", news=news, form=get_form)
    return render_template("get.html", form=get_form)


@app.route("/getAll", methods=['GET', 'POST'])
def get_all_page():
    news = News.query.all()
    return render_template("get_all.html", news=news)
