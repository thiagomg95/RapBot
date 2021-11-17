import lyricsgenius
import os
import shutil

"""
    Gets songs from Genius's API and saves them as json objects in /Rap Songs
    """

token = "QmR0s1Swep-mozpaJNmeMWD7PfsKf3NOWtscHVJqHcmJcQEEWaCdHwb9IEAq5aCM"
genius = lyricsgenius.Genius(token)


def move_songs_to_folder(folder_name):
    for item in os.listdir('../RapBot'):
        if os.path.isfile(os.path.join('../RapBot', item)) and item.endswith('.json'):
            shutil.move(item, '../RapBot/' + folder_name)


def get_songs(artist_name, max_songs):

    artist = genius.search_artist(artist_name, max_songs=max_songs, sort="title")
    for song in artist.songs:
        song.save_lyrics()
