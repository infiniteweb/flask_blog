from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)


@app.route("/")
def index():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    blog = data
    return render_template("index.html", blog=blog)


@app.route("/blog/<int:num>")
def blog_page(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    blog = data
    return render_template("blog.html", blog=blog, num=num)


if "__main__" == __name__:
    app.run(debug=True)
