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

     # AUTHENTICATION IN SPOTIPY
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # SEARCH FOR ARTISTS
    artist_name = artist
    results = sp.search(q=f'artist:{artist_name}', type='artist', limit=5)
    artists = results['artists']['items']
    artists_sorted = sorted(artists, key = lambda a: a['followers']['total'], reverse = True)
    if artists_sorted:
        print(f"Found {len(artists_sorted)} artists matching '{artist_name}':\n")
        for i, artist in enumerate(artists_sorted, start=1):
            print(f"{i}. - {artist['name']}   \n     Genres: {', '.join(artist['genres']) if artist['genres']  else 'No genres listed'}\n     Followers: {artist['followers']['total']}")
            # print(f"")
            # print("\n")
    else:
        print(f'No artist found for " {artist_name} " ')


########################## TOP 5 songs in country

def top_songs(artist, country):
    # AUTHENTICATION IN SPOTIPY
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # SEARCH FOR ARTISTS
    artist_name = artist
    results = sp.search(q=f'artist:{artist_name}', type='artist', limit=1)
    artists = results['artists']['items']

    if artists:
        artist_id = artist["id"]
        artist = artists[0]
    # SEARCH FOR SONGS
        top_tracks = sp.artist_top_tracks(artist_id, country)
        print(f"\nTop 5 most popular tracks of '{artist_name}' in {country} are:")
        for i, track in enumerate(top_tracks["tracks"][:5], start=1):
            print(f"{i}. {track['name']} - (popularity: {track['popularity']})")

    else: print(f"No artist name: '{artist}' found ... ")

##########################

def artist_in_genre(genre):

     # AUTHENTICATION IN SPOTIPY
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # SEARCH FOR ARTISTS
    genre = genre
    results = sp.search(q=f'genre:{genre}', type='artist', limit=15)
    artists = results['artists']['items']
    artists_sorted = sorted(artists, key = lambda a: a['followers']['total'], reverse = True)
    if artists_sorted:
        for i, artist in enumerate(artists_sorted, start=1):
            print(f"{i}. {artist['name']} - {artist['genres']} - total followers: {artist['followers']['total']}")


    else: print(f"No artists in genre: '{genre}' found ... ")


############################# MAIN

# search_for_artist('Howlin Wolf',)

# top_songs('Queen', 'PL')

artist_in_genre('blues')

