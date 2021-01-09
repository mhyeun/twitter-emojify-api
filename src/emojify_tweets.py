from flask import Flask, request, jsonify
from transform_tweet import transform_tweets
import json
import git

app = Flask(__name__)


@app.route("/health")
def health():
    return json.dumps({"success": True}), 200, {"ContentType": "application/json"}


@app.route("/emojify-tweets", methods=["GET"])
def send_emojified_tweets():
    if not request.args:
        return "Twitter username or number of tweets not given.", 400

    twitter_username = request.args.get("username")
    number_of_tweets = request.args.get("tweets")

    try:
        transformed_tweets = transform_tweets(twitter_username, number_of_tweets)
        return jsonify(transformed_tweets)
    except:
        return "Twitter username or number of tweets invalid.", 400


@app.route("/update_server", methods=["POST"])
def webhook():
    if request.method == "POST":
        repo = git.Repo("/mhyeun/twitter-emojify-api")
        origin = repo.remotes.origin

        origin.pull()
        return "Updated PythonAnywhere successfully", 200
    else:
        return "Wrong event type", 400
