import os
import json
import re

"""
    Composes the JSON dataset for identifying if it's a rap lyric or not
    """

line_list = []
lyric_list = []

for item in os.listdir('../RapBot/Songs'):
    if os.path.isfile(os.path.join('../RapBot/Songs', item)) and item.endswith('.json'):

        f = open('../RapBot/Songs/' + item, 'r')
        json_obj = json.load(f)

        line_list.append(json_obj["lyrics"])

for line in line_list:
    sub_lines = str(line).split('\n')
    for sub_line in sub_lines:
        re_match = re.search(r"^\w+", sub_line)
        try:
            lyric_list.append(re_match.string)
        except AttributeError:
            continue


f2 = open('Lyrics/rap_raw_lyrics.txt', 'a')
for lyric in lyric_list:
    f2.write(lyric + '\n')

# TODO: Pegar as linhas no documento rap_raw_lytics.txt e fazer um com linhas asssim:
#  {"lyric": XXXX, "is_rap": 1},

# TODO: Pegar esse arquivo e appendar exemplos com :
#  {"lyric": XXXX, "is_rap": 0},

# TODO: randomizar as linhas e fazer o root:

