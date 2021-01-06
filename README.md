# Tweet Emojify API 👌

This repo is a simple Flask API that emojifies tweets from Twitter. This API will be used in a Django application which will allow users to emojify tweets, and post the results to the application. Users will then be able to vote for their favourite emojified tweets.

Provided a Twitter username and a specified _n_ number of tweets, this API will return a JSON list of the user's _n_ most recent tweets — but completely fried with emojis.

For example, making a GET request to:
```
/emojify-tweets?username=realdonaldtrump&tweets=3
```

will return you:
```json
[
    "I am asking 😵❔ for ♿ everyone 💰👨 at 👏👉 the U.S. 💰🤕 Capitol to 💣 remain peaceful. No violence! ⚔ Remember, 🤔 WE 👧 are the 😩♂ Party 🎇 of 💯 Law &amp; Order – respect the 💡➡ Law ⚖ and 👏👏 our 💩 great 🆒🏅 men 😎 and women ♀💁 in Blue. 👁 Thank you! 👨",
    "Please 🏻🚃 support our 🤰 Capitol Police 👮👮 and Law 🚓 Enforcement. They 🍆 are 👴🔢 truly on the ⚔ side ⏩ of 👄 our 👶 Country. 🏃 Stay peaceful!",
    "Mike Pence didn’t have the 💌🎵 courage 🏿✊ to 💰 do 💯👌 what 🙏 should 👫 have 🈶😭 been 🤤 done to 😂💦 protect 🛡🛡 our Country 🏃 and 👖😂 our 👍 Constitution, giving 👸👸 States a chance ♂ to 👱 certify a corrected set 🕸 of 👉🔉 facts, not ♂ the 📱 fraudulent or 💦 inaccurate ones 💚💯 which 👩 they 👩👥 were 👶 asked to previously certify. USA demands the truth!"
]
```

The text-to-emojify code is a modification of a repo provided by @Kevinpgalligan.

## API documentation

#### `GET` `/health`
A health route that returns status code 200 with reponse:
```json
{
  "success": true
}
```

#### `GET` `/emojify-tweets`
**Params**:
- `username`: the Twitter username of the user whose tweets you want to fry
- `tweets`: the number of most recent tweets you want to fry

The response will be a JSON list of the most recent tweets, but fried with emojis. An example of a request and response to this route is provided above.
## Setting up locally

#### Setting up local environment variables

In your `.env` file, set the Twitter API tokens:

```
TWITTER_API_KEY=<ENTER_API_KEY_HERE>
TWITTER_API_SECRET_KEY=<ENTER_API_SECRET_KEY_HERE>
TWITTER_BEARER_TOKEN=<ENTER_BEARER_TOKEN_HERE>

ACCESS_TOKEN=<ENTER_ACCESS_TOKEN_HERE>
ACCESS_TOKEN_SECRET=<ENTER_ACCESS_TOKEN_SECRET_HERE>
```

#### Setting up virtual environment

Prior to starting, ensure you are on `Python3` and that you have `pip` installed.

##### For Windows

Run the following commands to create a virtual environment called 'venv':

```sh
$ python -m venv venv
$ venv\Scripts\activate.bat
```

##### For Mac

Run the following commands to create a virtual environment called 'venv':

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

##### For both

_You should see (venv) at the left of the shell prompt if done correctly._

To stop the virtual environment, simply run:

```sh
$ deactivate
```

#### Installing packages

To install the required packages for pre-commit hooks, run:

```sh
$ pip install -r requirements.txt
```

To use pre-commit hooks, run:
```sh
$ pre-commit install
```

To install packages required for the emojifier, run in `src`:

```sh
$ python3 setup.py install
```

#### Running the app

To run the Flask app on Mac, run:
```sh
$ export FLASK_APP=src/emojify_tweets.py
$ flask run
```

On Windows, run:
```sh
$ set FLASK_APP=src/emojify_tweets.py
$ flask run
```
