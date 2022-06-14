import tweepy
from frases import FRASES
from config import USERID, client
import random

def twittear_frase(api):
    frase = random.choice(FRASES)
    try:
        api.create_tweet(text=frase)
    except:
        api.create_tweet(text=random.choice(FRASES))
    return frase


def nuevo_sold(api):
    for follower in tweepy.Cursor(api.followers).items():
        api.create_tweet(text=f'Nuevo soldado! @{follower.username}')



def twittear(api):
    with open('favs.txt', 'r') as rf:
        favs = int(rf.readline())
        rf.close()
    with open('seguidores.txt', 'r') as rs:
        seguidores = [str(seg) for seg in rs]
        rs.close()
    favs_nuevos = 0
    for tweet in api.get_users_tweets(id=USERID).data:
        print(tweet.text)
        if api.get_liking_users(tweet.id).data:
            favs_nuevos += len(api.get_liking_users(tweet.id).data)
        else:
            print("este tuit no tiene favs nuevos")
    if favs_nuevos > favs:
        tw = twittear_frase(api)
        print(f'        {tw.upper()}')
    else:
        print('no hay favs nuevos')
    with open('favs.txt', 'w') as wf:
        wf.write(f'{favs_nuevos}\n {favs_nuevos}\n {favs_nuevos}\n {favs_nuevos}\n ')
        wf.close()

    for follower in api.get_users_followers(id=USERID).data:
        if str(follower.username) in seguidores:
            print('Soldado viejo')
        else:
            api.create_tweet(text=f'Nuevo soldado! @{follower.username}')
            with open('seguidores.txt', 'w') as ws:
                for i in seguidores:
                    ws.write(i)
                ws.close()

