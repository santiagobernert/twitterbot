import tweepy
import logging
import random
from config import USERID
from imagenes import IMAGENES

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()



def retweet(api,tweet):
    if tweet.user.id == USERID:
        return
    if not tweet.retweeted:
        try:
            tweet.retweet()
        except Exception as e:
            logger.error("Error on retweet", exc_info=True)

def fav(api, tweet):
    if tweet.user.id == USERID:
        return
    if not tweet.favorited:
        try:
            tweet.favorite()
        except Exception as e:
            logger.error("Error on fav", exc_info=True)

def responder(api, tweet, id_str):
    if tweet.user.id != USERID:
            try:
                api.update_status(f'Gracias por responder {tweet.user.name}', in_reply_to_status_id=id_str)
            except Exception as e:
                logger.error("Error al responder", exc_info=True)

def seguir(api, tweet):
    if tweet.user.id != USERID:
        if not tweet.user.following:
            try:
                api.create_friendship(user_id=tweet.user.id)
            except Exception as e:
                    logger.error("Error al seguir", exc_info=True)


def on_error(self, status):
    logger.error(status)

def interactuar(api):
    mentions = api.get_users_mentions(USERID)
    for mention in mentions.data:
        mention_id = mention.id
        retweet(api, mention_id)
        fav(api, mention_id)
        responder(api, mention_id, mention.id_str)
        seguir(api, mention_id)

if __name__ == "__main__":
    interactuar()
