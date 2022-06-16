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



def twittear(api):
    with open('favs.txt', 'r') as rf:
        favs = int(rf.readline())
        rf.close()
    with open('seguidores.txt', 'r') as rs:
        seguidores = [str(seg) for seg in rs]
        rs.close()
    with open('tweets.txt', 'r') as rt:
        tweets_viejos = [str(tw) for tw in rt]
        tweets_viejos = tweets_viejos[:-1]
        tweets_viejos = [x[:-2] for x in tweets_viejos]
        rt.close()
    favs_nuevos = 0
    for tweet in api.get_users_tweets(id=USERID).data:
            if str(tweet.id) not in tweets_viejos:
                if api.get_liking_users(tweet.id).data:
                    favs_nuevos += len(api.get_liking_users(tweet.id).data)
                    print('tweets viejos antes del tuit: ', tweets_viejos)
                    tweets_viejos.append(str(tweet.id))
                    print('tweets despues del tuit: ', tweets_viejos)
                    tweets_nuevos = list(dict.fromkeys(tweets_viejos))
                    print('tweets sin duplicados: ', tweets_nuevos)
                    if '000000\n' in tweets_nuevos:
                        tweets_nuevos.remove('000000\n')
                    print('tweets sin 0: ', tweets_nuevos)
    print('tweets: ' ,tweets_nuevos)
    with open('tweets.txt', 'w') as wt:
        for i in tweets_nuevos:
            wt.write(i)
            wt.write('\n')
        wt.close()
    if favs_nuevos > favs:
        tw = twittear_frase(api)
    with open('favs.txt', 'w') as wf:
        wf.write(f'{favs_nuevos}\n {favs_nuevos}\n {favs_nuevos}\n {favs_nuevos}\n ')
        wf.close()

    for follower in api.get_users_followers(id=USERID).data:
        if str(follower.username) not in seguidores:
            try:
                api.create_tweet(text=f'Nuevo soldado! @{follower.username}')
            except:
                print("error: tweet repetido")
            with open('seguidores.txt', 'w') as ws:
                seguidores.append(follower.username)
                seguidores_nuevos = list(dict.fromkeys(seguidores))
                for i in seguidores_nuevos:
                    ws.write(i)
                    ws.write('\n')
                ws.close()
        else:
            return

