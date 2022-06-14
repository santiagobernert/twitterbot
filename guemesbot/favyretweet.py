import tweepy
import logging
import random
from config import USERID
from imagenes import IMAGENES

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()



def retweet(api,tweet):
    if str(tweet.author_id) == USERID:
        return
    if not tweet.retweeted:
        try:
            api.retweet(tweet)
            print('retweet a ', tweet.text)
        except Exception as e:
            logger.error("Error on retweet", exc_info=True)

def fav(api, tweet):
    if str(tweet.author_id) == USERID:
        return
    if not tweet.favorited:
        try:
            api.like(tweet)
            print('like a ', tweet.text)
        except Exception as e:
            logger.error("Error on fav", exc_info=True)

def responder(api, tweet, id_str):
    if str(tweet.author_id) != USERID:
            try:
                api.create_tweet(text=f'Gracias por responder {tweet.user.name}', in_reply_to_tweet_id=id_str)
                print('rspondido a ', tweet.user.name)
            except Exception as e:
                logger.error("Error al responder", exc_info=True)

def seguir(api, tweet):
    if str(tweet.author_id) != USERID:
        if not tweet.user.following:
            try:
                api.follow_user(user_id=tweet.user.id)
                print('siguiendo a ', tweet.user.name)
            except Exception as e:
                    logger.error("Error al seguir", exc_info=True)


def on_error(self, status):
    logger.error(status)

def interactuar(api):
    mentions = api.get_users_mentions(USERID)
    for mention in mentions.data:
        print(mention.text)
        retweet(api, mention)
        fav(api, mention)
        responder(api, mention, mention.id_str)
        seguir(api, mention)

if __name__ == "__main__":
    interactuar()
