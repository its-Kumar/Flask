from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    html = """
        <html>
            <head>
                <title>First Flask Page</title>
            </head>
            <body>
            <h1> Welcome to my Flask Page..!!</h1>
            {author_ul}
            </body>
        </html>
    """
    authors = ["Alan Poe", "Jorge L. Borges", "Mark Twain", "Kumar shanu"]
    authors_list = "<ul>"
    authors_list += "\n".join(
        ["<li>{author}</li>".format(author=author) for author in authors]
    )
    authors_list += "</ul>"

    return html.format(author_ul=authors_list)
