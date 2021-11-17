from Resources.genius_api import *
from Resources.json_lyric_dataset_builder import *
from time import sleep

get_songs(artist_name="Eminem", max_songs=10)
move_songs_to_folder("Rap Songs")

get_songs(artist_name="2Pac", max_songs=10)
move_songs_to_folder("Rap Songs")

get_songs(artist_name="Kendrick Lamar", max_songs=10)
move_songs_to_folder("Rap Songs")

get_songs(artist_name="Wu Tang Clan", max_songs=10)
move_songs_to_folder("Rap Songs")

get_songs(artist_name="Taylor Swift", max_songs=10)
move_songs_to_folder("Non-Rap Songs")

get_songs(artist_name="Ed Sheeran", max_songs=10)
move_songs_to_folder("Non-Rap Songs")

get_songs(artist_name="Rihanna", max_songs=10)
move_songs_to_folder("Non-Rap Songs")

get_songs(artist_name="Harry Styles", max_songs=10)
move_songs_to_folder("Non-Rap Songs")

sleep(5)

compose_dataset()

sleep(5)

clean_temp_files()
clean_song_files()

# Agora olha na pasta Datasets e veja que tem um dataset novo
