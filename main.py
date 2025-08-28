from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

################################## loading credentials
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# print(client_id, client_secret)

######################### GET TOKEN FROM SPOTIFY

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

############################# HEADER with TOKEN for further use with API

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

############################## search for artist

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f'?q={artist_name}&type=artist'
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result) == 0 :
        print("No artis with given name ... ")
        return None

    return json_result

############################# search for song -

def search_for_song(token, song_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f'?q={song_name}&type=track'
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)['tracks']['items']

    if len(json_result) == 0 :
        print("No song with given name ... ")
        return None

    return json_result

############################ listing of artists

def list_of_artists(result):
    print(f'\n#######################\nNumber of artists: {len(result)} \n#######################')
    for i in range (len(result)):
        print(f'{i+1}. \nName: {result[i]["name"]} \nGenres: {result[i]["genres"]} \n artist id: {result[i]["id"]} ')

    print('#######################')

###################################### list of artist by given song title
def artist_of_song(result):
    print(f'\n#######################\nArtists of your song: \n#######################')
    for i in range(len(result)):
        print(f'{i+1}. {result[i]["artists"][0]["name"]} - {result[i]["name"]}\n '
              f'Popularity: {result[i]["popularity"]}\n' )

    print('#######################')

################################ list of songs by artist

def get_songs_by_artist(token, artist_id):
    url = f'https://api.spotify.com/v1/artist/{artist_id}/top-tracks?country=PL'
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

###################################### MAIN

token = get_token()
#
# artist = search_for_artist(token, "William Clarke")
# list_of_artists(artist)

song  = search_for_song(token, 'Cry me a river ')
print(song[0].keys())
artist_of_song(song)



















