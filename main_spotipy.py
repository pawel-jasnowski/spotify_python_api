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
countries = list(sp.available_markets()['markets'])   # country codes on available on SPOTIFY

# print(client_id, client_secret)


############################## Country list available on SPOTIFY
def list_countries():
    print("\nAvailable Spotify country codes:\n")
    print(", ".join(countries))

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
            print(f"{i}. - {artist['name']}\n     Genres: {', '.join(artist['genres']) if artist['genres']  else 'No genres listed'}\n     Followers: {artist['followers']['total']}\n     Popularity: {artist['popularity']}")
            # print(f"")
            # print("\n")
    else:
        print(f'No artist found for " {artist_name} " ')


########################## TOP songs in given country

def top_songs(artist, country):

    # SEARCH FOR ARTISTS
    country = country.upper()
    if country not in countries:
        print("Wrong country code")
        return

    artist_name = artist
    results = sp.search(q=f'artist:{artist_name}', type='artist', limit=1)
    artists = results['artists']['items']
    if not artists:
        print(f"No artist name: '{artist}' found ... ")
        return

    # SEARCH FOR SONGS
    artist_id = artists[0]["id"]
    top_tracks = sp.artist_top_tracks(artist_id, country)

    print(f"\nTop 5 most popular tracks of '{artist_name}' in {country} are:")
    for i, track in enumerate(top_tracks["tracks"][:5], start=1):
        print(f"{i}. {track['name']} - (popularity: {track['popularity']})")



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

################### Search Albums from artist

def artist_albums(artist):
    # SEARCH FOR albums
    results = sp.search(q=f'artist:{artist}', type='artist', limit=1)
    artists = results['artists']['items']

    if not artists:
        print(f'No artist found for "{artist}"')
        return

    artist_id = artists[0]['id']
    albums = sp.artist_albums(artist_id, album_type='album')

    if not albums or not albums.get('items'):
        print(f'No albums found for "{artist}"')
        return

    print(f"\nAlbums by {artist}:")
    for i, album in enumerate(albums['items'][:20], start=1):
        print(f"{i}. {album['name']} - ({album['release_date']})")



#################### next action
def next_action():

    """Ask user what to do next"""

    input("Press Enter to continue...")
    while True:
        print("\n************ What do you want to do next? ************\n")
        print("1. Back to main menu: \n")
        print("2. EXIT\n")

        choice = input("Enter your choice: \n").strip()
        if choice =="1":
            return True # go back to main menu
        elif choice == "2":
            print("See you again soon\n")
            return False # exit and close the main
        else: print("Invalid choice, try again\n")


############################# MAIN

# search_for_artist('Howlin Wolf',)

# top_songs('Queen', 'US')

# artist_in_genre('blues')

def main():
    running = True
    while running:
        print('\n************ SPOTIFY CLI Explorer ************\n')
        print('1. Search by ARTIST\n')
        print('2. Search by TOP SONG of ARTIST in given COUNTRY\n')
        print('3. Search by TOP ARTIST by GENRE\n')
        print('4. Search by ALBUMS of ARTIST\n')
        print('5. EXIT\n')

        choice = input("ENTER number of your choice: ").strip()

        if choice == '1':
            name = input("Enter artist name: ").strip()
            search_for_artist(name)

        elif choice =='2':
            name = input("Enter artist name: ").strip()
            list_countries()
            country = input("\nEnter country code (i.e. PL/US/IT/GE) : " ).strip().upper()
            top_songs(name, country)

        elif choice =='3':
            genre = input("Enter genre: ").strip()
            artist_in_genre(genre)

        elif choice == '4':
            artist = input("Enter artist name: ").strip()
            artist_albums(artist)

        elif choice == '5':
            print("See you again soon")
            break

        else: print("Invalid choice. Try again. \n")

        running = next_action()



if __name__ == "__main__":
    main()
#

######################## TEMP below ####################33
# artist_name = 'asdfghjklqwerty'
# results = sp.search(q=f'artist:{artist_name}', type='artist', limit=1)
# artists = results['artists']['items']
# print(json.dumps(results, indent=2))

# def artist_albums_temp(artist):
#     # SEARCH FOR albums
#     results = sp.search(q=f'artist:{artist}', type='artist', limit=1)
#     artists = results['artists']['items']
#     artist_id = artists[0]['id']
#     albums = sp.artist_albums(artist_id, album_type='album')
#
#
#
# artist_albums_temp('tupac')