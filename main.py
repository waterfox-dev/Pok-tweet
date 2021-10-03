from pokemon import Generator
from to_image import toimage
from datetime import datetime
from keep_alive import keep_alive
from cleaner import clean

import tweepy
import json
import time


with open("api_config.json") as config_file: config_file = json.load(config_file)

consumer_key        = config_file['api_key']
consumer_secret_key = config_file['api_secret_key']
access_token        = config_file['access_token']
access_token_secret = config_file['access_token_secret']
connect             = True

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

generator = Generator()

while connect :
    
    keep_alive()

    while True :

        current_hour = datetime.now() 

        if (current_hour.hour + 2 == 22 or current_hour.hour + 2 == 10) and (current_hour.minute == 00 or current_hour.minute == 1):
            
            try :
                pokemon_of_day = generator.random_pokemon()

                toimage(pokemon_of_day.image_url)

                media  = api.media_upload(f'{pokemon_of_day.id}.png')
                tweet = f"Le pokémon du jour est {pokemon_of_day.name} ({pokemon_of_day.id}) \n{pokemon_of_day.description}"
                post_result = api.update_status(status=tweet, media_ids=[media.media_id])
                clean(pokemon_of_day.id)
                time.sleep(120)

            except :
                print("An error was occured during the tweet sending")

        else :
            time.sleep(30)