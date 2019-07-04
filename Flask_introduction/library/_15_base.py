from flask import Flask, request, render_template
import sqlite3
from . import config

app = Flask(__name__)


def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('inheritance/child_template_form.html')
    elif request.method == 'POST':
        db = connect_db()
        sql_query = """
            INSERT INTO book ("title", "isbn", "author_id") VALUES (:title, :isbn, :author_id);
        """
        db.execute(sql_query, {
            'title': request.form['title'],
            'isbn': request.form['isbn'],
            'author_id': int(request.form['author']),
        })
        db.commit()
        return "The new book {} was correctly saved".format(request.form['title'])
