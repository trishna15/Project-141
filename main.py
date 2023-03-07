from flask import Flask, jsonify, request
import csv

all_articles = []

with open("articles.csv",encoding="utf8") as f:
    reader = csv.reader(f)
    data =list(reader)

    all_articles = data[1:]

liked_artciles = []
unliked_articles = []

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data":all_articles[0],
        "status": "success"

    })

@app.route("/liked-articles",methods=["POST"])
def liked_articles():
    articles = all_articles[0]
    liked_artciles.append(articles)
    all_articles.pop(0)
    return jsonify({
        "status":"success"
    }),201

 

if __name__ == "__main__":
    app.run()

