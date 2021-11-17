import lyricsgenius
import os
import shutil

"""
    Gets songs from Genius's API and saves them as json objects in /Rap Songs
    """

token = "QmR0s1Swep-mozpaJNmeMWD7PfsKf3NOWtscHVJqHcmJcQEEWaCdHwb9IEAq5aCM"
genius = lyricsgenius.Genius(token)


def get_songs(is_rap_artist, artist_name, max_songs):

    if is_rap_artist:

        artist = genius.search_artist(artist_name, max_songs=max_songs, sort="title")

        for song in artist.songs:
            song.save_lyrics()

        for item in os.listdir('..'):
            if os.path.isfile(os.path.join('..', item)) and item.endswith('.json'):
                print(item)
                shutil.move(item, '../Rap Songs')
    else:
        artist = genius.search_artist(artist_name, max_songs=max_songs, sort="title")

        for song in artist.songs:
            song.save_lyrics()

        for item in os.listdir('..'):
            if os.path.isfile(os.path.join('..', item)) and item.endswith('.json'):
                print(item)
                shutil.move(item, '../Non-Rap Songs')
