from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import base64
from requests import post
import json

##################################
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

print(client_id, client_secret)

############################## SPOTIPY

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
#     client_id = client_id,
#     client_secret = client_secret,
#     redirect_url = "http://localhost:8888/callback/",
#     scope == "user-library-read"  # permission scopes
# ))
#
#