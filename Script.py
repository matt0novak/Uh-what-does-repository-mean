import tweepy
auth = tweepy.OAuthHandler("J2ICqfRwWoIWccpETtzimBhN3", "rZOiJnFbOoIgKqLp5NA4ALtCZdXa29MrijHX7QBmixahifTMjZ")
auth.set_access_token("889428062282100736-YPP6iroA0Jdo3CtbpgfJq9QVuP60F1v", "iF2oWraG0L9Sk0P0UkfuPBotZG1auDi5glerMpyqZyCO8")
api = tweepy.API(auth)
tweet = input("Conjure Up A Tweet: ")
api.update_status(status =(tweet))
print ("Done!")