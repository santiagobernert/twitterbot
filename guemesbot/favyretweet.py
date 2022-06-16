import tweepy
import random
from config import USERID




def retweet(api,tweet):
    with open('retweets.txt', 'r') as rrt:
        retweets = [str(rtw) for rtw in rrt]
        retweets = retweets[:-1]
        retweets = [x[:-2] for x in retweets]
        rrt.close()
    if tweet.id in retweets:
        return
    if int(tweet.author_id) == USERID:
        return
    if str(tweet.id) not in retweets:
        try:
            api.retweet(tweet.id)
            print('retweet a ', tweet.text)
            retweets.append(str(tweet.id))
            print('retweets nuevs: ', retweets)
            retweets_nuevos = list(dict.fromkeys(retweets))
            print('retweets nuevs sin duplicados: ', retweets_nuevos)
            if '000000\n' in retweets_nuevos:
                retweets_nuevos.remove('000000\n')
            print('retweets nuevs sin 0: ', retweets_nuevos)
            print('retweets: ' , retweets_nuevos)
            with open('retweets.txt', 'w') as wrt:
                for i in retweets_nuevos:
                    wrt.write(i)
                    wrt.write('\n')
                print(retweets)
                wrt.close()
        except Exception as e:
            print("Error on retweet")

def fav(api, tweet):
    with open('misfavs.txt', 'r') as rmf:
        favs_viejos = [str(fv) for fv in rmf]
        favs_viejos = favs_viejos[:-1]
        favs_viejos = [x[:-2] for x in favs_viejos]
        rmf.close()
    if int(tweet.author_id) == USERID:
        return
    if str(tweet.id) not in favs_viejos:
        try:
            api.like(tweet.id)
            print('like a ', tweet.text)
            favs_viejos.append(str(tweet.id))
            favs_nuevos = list(dict.fromkeys(favs_viejos))
            if '000000\n' in favs_nuevos:
                favs_nuevos.remove('000000\n')
            with open('misfavs.txt', 'w') as wmf:
                for i in favs_nuevos:
                    wmf.write(i)
                    wmf.write('\n')
                wmf.close()
        except Exception as e:
            print("Error on fav")

def responder(api, tweet):
    if int(tweet.author_id) != USERID:
        try:
            api.create_tweet(text=f'Gracias por responder {api.get_user(tweet.author_id).name}', in_reply_to_tweet_id=tweet.id)
            print('respondido a ', api.get_user(tweet.author_id).name)
        except Exception as e:
            print("Error al responder")

def seguir(api, tweet):
    if int(tweet.author_id) != USERID:
        try:
            api.follow_user(user_id=tweet.author_id)
            print('siguiendo a ', api.get_user(tweet.author_id).name)
        except Exception as e:
                print("Error al seguir")


def interactuar(api):
    mentions = api.get_users_mentions(USERID, expansions='author_id')
    if mentions.data is not None:
        for mention in mentions.data:
            retweet(api, mention)
            fav(api, mention)
            responder(api, mention)
            seguir(api, mention)

if __name__ == "__main__":
    interactuar()
