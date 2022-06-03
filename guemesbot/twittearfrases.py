import tweepy, logging
from frases import FRASES
from imagenes import IMAGENES
from config import USERID
import random
logger = logging.getLogger()

def twittear_frase(api):
    api.update_status(random.choice(random.choice([FRASES, IMAGENES])))


favs = 0

def twittear(api):
    favs_nuevos = 0
    for tweet in api.get_users_tweets(id=USERID).data:
        favs_nuevos += len(api.get_liking_users(tweet).data)
        if favs_nuevos > favs:
            favs = favs_nuevos
            twittear_frase(api)
            break
    for follower in tweepy.Cursor(api.followers).items():
        logger.info(f"Nuevo soldado {follower.name}")
        api.update_status(f'Nuevo soldado! @{follower.username}')

if __name__ == "__main__":
    twittear()