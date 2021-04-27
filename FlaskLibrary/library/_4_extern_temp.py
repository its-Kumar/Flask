from flask import Flask, render_template

app = Flask(__name__, template_folder="/")


@app.route("/")
def hello_world():
    library_name = "Poe"
    return render_template("index.html", library_name=library_name)
