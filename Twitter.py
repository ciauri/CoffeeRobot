# Twitter.py
# Author: Austin Ayers
# Uses Twitter API to tweet updates about the coffee

import tweepy

class Twitter():
    """
    Twitter class, simply a function to tweet a string or a boolean update on whether or not the coffee is ready.
    """
    def __init__(self):
        """
        Initializes Twitter, establishes authentication w/ following keys.
        """
        cfg = {
                "consumer_key"        : "XDAEJtqe2vjSj94egQq4BaCXX",
                "consumer_secret"     : "XvgRdAaTU1vDpWdwquKMbgyk0HIcaCNWxXjoWtXOAU8Y4oKuaE",
                "access_token"        : "720366080250630145-z819wKYjvqncLeYBcg46K9rPtxNh8mI",
                "access_token_secret" : "dMbGofZ1uWYJ8hqmI4BsveT0rQGvdkFxoVLee3e9Hi7lt"
        }
        api = get_api(cfg)
    def get_api(self, cfg):
        auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
        auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
        return tweepy.API(auth)
    def tweet(self, message):
        """
        Tweets the following string message
        """
        status = api.update_status(status=message)
    def tweet(self, isEmpty):
        """
        Tweets status of the coffee pot.
        isEmpty --- Boolean value (true - coffee pot is empty) (false - coffee pot is full)
        """
        if(isEmpty):
            msg = "THE COFFEE POT IS EMPTY."
        else:
            msg = "THE COFFEE POT HAS COFFEE IN IT. DRINK, HUMANS."
        status = api.update_status(status=msg)
