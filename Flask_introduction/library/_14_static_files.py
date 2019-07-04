from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('forms/form_with_static.html')
    elif request.method == 'POST':
        kwargs = {
            'title': request.form['title'],
            'isbn': request.form['isbn'],
            'author': request.form['author'],
            'secret_key': request.form['SECRET_KEY'],
            'submit_value': request.form['submit'],
        }
        return render_template(
            'forms/basic_form_result.html', **kwargs)
