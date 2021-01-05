from dotenv import load_dotenv

load_dotenv()

import os

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
print(TWITTER_API_KEY)
