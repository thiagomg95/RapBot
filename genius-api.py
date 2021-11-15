import lyricsgenius
import os
import shutil

"""
    Gets songs from Genius's API and saves them as json objects in /Songs
    """

artist_name = "Eminem"
max_songs = 5

token = "QmR0s1Swep-mozpaJNmeMWD7PfsKf3NOWtscHVJqHcmJcQEEWaCdHwb9IEAq5aCM"
genius = lyricsgenius.Genius(token)

artist = genius.search_artist(artist_name, max_songs=max_songs, sort="title")

for song in artist.songs:
    song.save_lyrics()

for item in os.listdir('../RapBot'):
    if os.path.isfile(os.path.join('../RapBot', item)) and item.endswith('.json'):
        print(item)
        shutil.move(item, 'Songs')
