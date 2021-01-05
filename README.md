# Tweet Bot

This app is the API for the Twitter Emojify Bot. This app performs the pulling of tweets via Twitter API and converts the tweet into a emoji clusterfuck — once converted, the API will send the transformed tweet to our Django app for display and storage.

Emojify code provided by @Kevinpgalligan.
## Setting up locally

#### Setting up local environment variables

In your `.env` file, set the Twitter API tokens:

```
TWITTER_API_KEY=<ENTER_API_KEY_HERE>
TWITTER_API_SECRET_KEY=<ENTER_API_SECRET_KEY_HERE>
TWITTER_BEARER_TOKEN=<ENTER_BEARER_TOKEN_HERE>
```

#### Setting up virtual environment

Prior to starting, ensure you are on `Python3` and that you have `pip` installed.

##### For Windows

Jay please add a section here once you figure it out.

##### For Mac

Run the following commands to create a virtual environment called 'venv':

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

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

To install packages required for the emojifier, run:

```sh
$ python3 src/setup.py install
```
