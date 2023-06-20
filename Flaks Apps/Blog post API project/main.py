import requests
from flask import Flask, render_template
from post import Post


app = Flask(__name__)

url_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url_endpoint)
response.raise_for_status()
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:id>/")
def get_post(id):
    return render_template('post.html', post=all_posts[int(id)-1])


if __name__ == "__main__":
    app.run()