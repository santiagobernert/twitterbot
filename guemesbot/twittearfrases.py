import tweepy, logging
from frases import FRASES
from imagenes import IMAGENES
from config import USERID, client
import random
logger = logging.getLogger()

def twittear_frase(api):
    frase = random.choice(FRASES)
    api.create_tweet(text=frase)
    return frase

def twittear_imagen(api):
    imagen = random.choice(IMAGENES)
    api = tweepy.API(auth)

    media = api.media_upload(filename=imagen)
    print("MEDIA: ", media)

    api.update_status(media_ids=[media.media_id_string])

def nuevo_sold(api):
    for follower in tweepy.Cursor(api.followers).items():
        logger.info(f"Nuevo soldado {follower.name}")
        api.create_tweet(text=f'Nuevo soldado! @{follower.username}')


with open('C:/Users/ETEC/Documents/gringo/twitterbot/guemesbot/favs.txt', 'r') as r:
    favs = int(r.readline())
    r.close()
seguidores = ['Mauro017975703']

def twittear(api):
    global favs, seguidores
    favs_nuevos = 0
    for tweet in api.get_users_tweets(id=USERID).data:
        print(tweet.text)
        if api.get_liking_users(tweet.id).data:
            favs_nuevos += len(api.get_liking_users(tweet.id).data)
            if favs_nuevos > favs:
                tw = twittear_frase(api)
                print(f'        {tw.upper()}')
                with open('favs.txt', 'w') as w:
                    w.write(str(favs+favs_nuevos))
                    w.close()
                break
            else:
                print("este tuit no tiene favs nuevos")
    else:
        print('no hay favs nuevos')

    for follower in api.get_users_followers(id=USERID).data:
        if str(follower.username) in seguidores:
            print('Soldado viejo')
        else:
            logger.info(f"Nuevo soldado {follower.name}")
            api.create_tweet(text=f'Nuevo soldado! @{follower.username}')
            seguidores.append(str(follower.username))

if __name__ == "__main__":
    twittear_frase(client)