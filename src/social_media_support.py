```python
import tweepy
from customer_support import resolveIssue

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_key = "YOUR_ACCESS_KEY"
access_secret = "YOUR_ACCESS_SECRET"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# Create API object
api = tweepy.API(auth)

class SocialMediaSupport:

    def __init__(self):
        self.api = api

    def listen_to_tweets(self, keywords):
        """
        This function listens to tweets with specific keywords and responds to them.
        """
        class MyStreamListener(tweepy.StreamListener):

            def on_status(self, status):
                print(status.text)
                issue = status.text
                response = resolveIssue(issue)
                api.update_status(status=response, in_reply_to_status_id=status.id)

        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

        myStream.filter(track=keywords)

    def post_updates(self, update):
        """
        This function posts updates on Twitter.
        """
        api.update_status(update)

social_media_support = SocialMediaSupport()
```