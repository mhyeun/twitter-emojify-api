from flask import Flask, request, jsonify
from transform_tweet import transform_tweets
import json

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
