import tweepy

def post_tweet(tweet):

    twitter_auth_keys = {
        "consumer_key"        : "MuB83Cu0HN2qWhExgBtIVhc6s",
        "consumer_secret"     : "RfQGDVX9JJst9GMOOPuqOoQAJVjX8m1Ab8Gi4Rb7amiZkq6FNW",
        "access_token"        : "1566118237221392386-UMJ9xoZWNkSowiVB7vV69ImXnLqcUh",
        "access_token_secret" : "KAJziFsOahmPx9bDwpYpLzMmkaxbuBrZuiCuJjqtlqIQO"
    }

    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )

    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )

    api = tweepy.API(auth)

    status = api.update_status(status=tweet)


if __name__ == "__main__":
    tweet = "Hello World! Subscribe if you want to know what's the trendiest outfit to WAIR :D"
    post_tweet(tweet)