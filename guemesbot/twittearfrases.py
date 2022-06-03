import tweepy, logging
from frases import FRASES
from imagenes import IMAGENES
from config import USERID, client
import random
logger = logging.getLogger()

def twittear_frase(api):
    frase = random.choice(FRASES)
    print(frase)
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


favs = 0

def twittear(api):
    global favs
    favs_nuevos = 0
    for tweet in api.get_users_tweets(id=USERID).data:
        print(tweet.text)
        favs_nuevos += len(api.get_liking_users(tweet.id).data)
        if favs_nuevos > favs:
            tw = twittear_frase(api)
            print(f'        {tw.upper()}')
            favs = favs_nuevos
            break
        else:
            print('no hay favs nuevos')
    for follower in api.get_users_followers(id=USERID).data:
        logger.info(f"Nuevo soldado {follower.name}")
        api.create_tweet(text=f'Nuevo soldado! @{follower.username}')

if __name__ == "__main__":
    twittear_frase(client)