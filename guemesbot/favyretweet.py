import tweepy
import random
from config import USERID




def retweet(api,tweet):
    if int(tweet.author_id) == USERID:
        return
    try:
        api.retweet(tweet.id)
        print('retweet a ', tweet.text)
    except Exception as e:
        print("Error on retweet")

def fav(api, tweet):
    if int(tweet.author_id) == USERID:
        return
    try:
        api.like(tweet.id)
        print('like a ', tweet.text)
    except Exception as e:
        print("Error on fav")

def responder(api, tweet):
    if int(tweet.author_id) != USERID:
        try:
            print(f'Gracias por responder {api.get_user(tweet.author_id).name} in reply to {tweet.id}')
            api.create_tweet(text=f'Gracias por responder {api.get_user(tweet.author_id).name}', in_reply_to_tweet_id=tweet.id)
            print('respondido a ', api.get_user(tweet.author_id).name)
        except Exception as e:
            print("Error al responder")

def seguir(api, tweet):
    if int(tweet.author_id) != USERID:
        try:
            print(f'Seguir a {api.get_user(tweet.author_id).name} in reply to {tweet.id}')
            api.follow_user(user_id=tweet.author_id)
            print('siguiendo a ', api.get_user(tweet.author_id).name)
        except Exception as e:
                print("Error al seguir")


def on_error(self, status):
    print(status)

def interactuar(api):
    mentions = api.get_users_mentions(USERID, expansions='author_id')
    for mention in mentions.data:
        print(mention.text)
        retweet(api, mention)
        fav(api, mention)
        responder(api, mention)
        seguir(api, mention)

if __name__ == "__main__":
    interactuar()
