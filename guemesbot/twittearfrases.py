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




def twittear(api):
    with open('guemesbot/favs.txt', 'r') as rf:
        favs = int(rf.readline())
        rf.close()
    with open('guemesbot/seguidores.txt', 'r') as rs:
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
    with open('guemesbot/favs.txt', 'w') as wf:
        wf.write(str(favs_nuevos))
        wf.close()

    for follower in api.get_users_followers(id=USERID).data:
        if str(follower.username) in seguidores:
            print('Soldado viejo')
        else:
            logger.info(f"Nuevo soldado {follower.name}")
            api.create_tweet(text=f'Nuevo soldado! @{follower.username}')
            with open('guemesbot/seguidores.txt', 'r') as ws:
                ws.write(seguidores)
                ws.close()

#if __name__ == "__main__":
#    twittear_frase(client)