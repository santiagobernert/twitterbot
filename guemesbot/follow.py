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
            api.follow_user(follower)


def seguir(api):
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    seguir()