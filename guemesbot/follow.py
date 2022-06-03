import tweepy
import logging
import time
from config import USERID

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in api.get_users_followers(id=USERID):
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow_user()

def follow_likers(api, tweet):
    users = api.get_liking_users(tweet)
    for user in users:
        if not user.following:
            logger.info(f"Following {user.name}")
            user.follow_user()

def seguir(api):
    while True:
        follow_followers(api)
        tweets = api.get_users_tweets()
        for tweet in tweets:
            follow_likers(api, tweet)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()