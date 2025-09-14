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


############################## SPOTIPY
# AUTHENTICATION IN SPOTIPY
# Authenticate with Spotify using Client Credentials Flow

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# print(client_id, client_secret)


#######################################search for artists
def search_for_artist(artist):

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


########################## TOP 5 songs in given country

def top_songs(artist, country):

    # SEARCH FOR ARTISTS
    artist_name = artist
    results = sp.search(q=f'artist:{artist_name}', type='artist', limit=1)
    artists = results['artists']['items'][0]

    if artists:
        artist_id = artists["id"]
    # SEARCH FOR SONGS
        top_tracks = sp.artist_top_tracks(artist_id, country)
        print(f"\nTop 5 most popular tracks of '{artist_name}' in {country} are:")
        for i, track in enumerate(top_tracks["tracks"][:5], start=1):
            print(f"{i}. {track['name']} - (popularity: {track['popularity']})")

    else: print(f"No artist name: '{artist}' found ... ")

########################## ARTISTS BY GENRE

def artist_in_genre(genre):

    # SEARCH FOR ARTISTS
    genre = genre
    results = sp.search(q=f'genre:{genre}', type='artist')
    artists = results['artists']['items']
    artists_sorted = sorted(artists, key = lambda a: a['followers']['total'], reverse = True)
    if artists_sorted:
        print(f"\nTop artists in '{genre}' are:\n")
        for i, artist in enumerate(artists_sorted, start=1):
            print(f"{i}. {artist['name']} - genres: {', '.join(artist['genres']) if artist['genres'] else 'No genres listed'} - total followers: {artist['followers']['total']}")


    else: print(f"No artists in genre: '{genre}' found ... ")

#################### next action

def next_action():

    """Ask user what to do next"""

    while True:
        print("\nWhat do you want to do next?\n")
        print("1. Back to main menu: \n")
        print("2. EXIT\n")

        choice = input("Enter your choice: \n").strip()
        if choice =="1":
            return True # go back to main menu
        elif choice == "2":
            print("See you again soon\n")
            return False
        else: print("Invalid choice, try again\n")


############################# MAIN

# search_for_artist('Howlin Wolf',)

# top_songs('Queen', 'US')

# artist_in_genre('blues')

def main():
    while True:
        print('\n************ SPOTIFY CLI Explorer ************\n')
        print('1. Search by ARTIST\n')
        print('2. Search by TOP SONG of ARTIST in given COUNTRY\n')
        print('3. Search by TOP ARTIST by GENRE\n')
        print('4. EXIT\n')

        choice = input("ENTER number of yout choice:   ").strip()

        if choice == '1':
            name = input("Enter artist name: ").strip()
            search_for_artist(name)
            if not next_action():
                break
        elif choice =='2':
            name = input("Enter artist name: ").strip()
            country = input("Enter coutnry code: " ).strip()
            top_songs(name, country)
            if not next_action():
                break
        elif choice =='3':
            genre = input("Enter genre: ").strip()
            artist_in_genre(genre)
            if not next_action():
                break
        elif choice == '4':
            print("See you again soon")
            break
        else: print("Invalid choice. Try again. \n")



if __name__ == "__main__":
    main()
