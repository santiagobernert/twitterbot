import tweepy 
import logging
  

logger = logging.getLogger()

USERID = 1532322971251097602
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAM0PdQEAAAAA5l2WGoFinIg8w7FFjBBhaSV%2BoQE%3D3NDpHfgY2tiCAGsXesu5jTqKIAqPNSGtWb6qhduwoG7NaZQMee'
client = tweepy.Client(bearer_token=bearer_token)


def crear_api():  
    
    auth = tweepy.OAuthHandler('byMMYinY8VDXwfiSftDSCxVCb', 'vUkgkzkmXsA10i647Nfjx7zOrVrISgj4VKTD5MUa9BypKC8NQY') 
    auth.set_access_token('1532322971251097602-PVDqt9wp0aLx6KVtN1Sh9HVsVbmlVa', '1vaXsVE5uDcgHoQB5ilh8hGBjPo9H922EBylnNwPbLAr4') 
    api = tweepy.API(auth) 
    api.update_profile(name='Martín Miguel de Güemes', description='Bot del General Güemes', location='Salta, Argentina')
    
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creando API", exc_info=True)
        raise e
    logger.info("API creada")
    return api
  

  
