from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import base64
from requests import post
import json

##################################
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# print(client_id, client_secret)

############################## SPOTIPY

# Authenticate with Spotify using Client Credentials Flow

#search for artists
def search_for_artist(artist):
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    artist_name = artist
    results = sp.search(q=f'artist:{artist_name}', type='artist')
    artists = results['artists']['items']

    if artists:
        print(f"Found {len(artists)} artists matching '{artist_name}':\n")
        for i, artist in enumerate(artists, start=1):
            print(f"{i}. - {artist['name']}   \n     Genres: {', '.join(artist['genres']) if artist['genres']  else 'No genres listed'}\n     Followers: {artist['followers']['total']}")
            # print(f"")
            # print("\n")
    else:
        print(f'No artist found for {artist_name}')

############################# MAIN

search_for_artist('AC/DC')
