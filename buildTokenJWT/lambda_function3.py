from jose import jwt
import math
import time

def lambda_handler(event, context):
    
    def jwt_sign_url(media_key, host='http://cdn.jwplayer.com/v2/', route):
        secret = "YftieMszPDp267sRkEE9xH2c"
        exp = math.ceil((time.time() + 3600)/180) * 180 # Link is valid for 1hr but normalized to 3 minutes to promote better caching

        token_body = {
            "resource": "/v2/" + route + "/" + media_key,
            "exp": exp
        }
    
        url = host + media_key + '?sig={signature}'.format(host=host, signature=jwt.encode(token_body, secret, algorithm='HS256'))
        return url
        
    
    video_key = event['queryStringParameters']['media_id']# video key
    playlist_key = event['queryStringParameters']['playlist_id']# playlist key

    if playlist_key != "":
        signed_url = jwt_sign_url(video_key, "playlists")
    else:
        signed_url = jwt_sign_url(video_key, "media")
    
    listOfDomains = ['http://anillosguillen.com', 'https://anillosguillen.com', 'http://localhost', 'https://se.jwplayer.com']
    
    if 'origin' in event['headers'] and event['headers']['origin'] in listOfDomains :
        return signed_url
    else:
        return "Broken"