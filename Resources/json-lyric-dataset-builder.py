import os
import json
import re
import random

"""
    Composes the JSON dataset for identifying if it's a rap lyric or not
    """


def compose_unformatted_json():
    rap_line_list = []
    rap_lyric_list = []
    non_rap_line_list = []
    non_rap_lyric_list = []

    for item in os.listdir('../Rap Songs'):
        if os.path.isfile(os.path.join('../Rap Songs', item)) and item.endswith('.json'):
            f = open('../RapBot/Rap Songs/' + item, 'r')
            json_obj = json.load(f)

            rap_line_list.append(json_obj["lyrics"])

    for line in rap_line_list:
        sub_lines = str(line).split('\n')
        for sub_line in sub_lines:
            re_match = re.search(r"^\w+", sub_line)

            if not sub_line.__contains__("\""):
                try:
                    rap_lyric_list.append(re_match.string)
                except AttributeError:
                    continue

    f2 = open('Lyrics/unformatted_json.txt', 'a')

    for lyric in rap_lyric_list:
        f2.write("{\"lyric\": \"" + lyric + "\", \"is_rap\": " + str(1) + "},\n")

    for item in os.listdir('../Non-Rap Songs'):
        if os.path.isfile(os.path.join('../Non-Rap Songs', item)) and item.endswith('.json'):
            f = open('../RapBot/Non-Rap Songs/' + item, 'r')
            json_obj = json.load(f)

            non_rap_line_list.append(json_obj["lyrics"])

    for line in non_rap_line_list:
        sub_lines = str(line).split('\n')
        for sub_line in sub_lines:
            re_match = re.search(r"^\w+", sub_line)

            if not sub_line.__contains__("\""):
                try:
                    non_rap_lyric_list.append(re_match.string)
                except AttributeError:
                    continue

    f2 = open('Lyrics/unformatted_json.txt', 'a')

    for lyric in non_rap_lyric_list:
        f2.write("{\"lyric\": \"" + lyric + "\", \"is_rap\": " + str(0) + "},\n")


def randomize_unformatted_json():

    lines = open('Lyrics/unformatted_json.txt', 'r').readlines()
    random.shuffle(lines)
    open('Lyrics/randomized_unformatted_json.txt', 'w').writelines(lines)


def format_json():

    un_formatted_json_lines = open('Lyrics/randomized_unformatted_json.txt', 'r').readlines()
    formatted_json = open('Datasets/rap_training_dataset.json', 'w')

    formatted_json.write("{\"root\": [")
    formatted_json.writelines(un_formatted_json_lines)
    formatted_json.write("{\"lyric\": \"But the cops getting dropped by the gun shot\", \"is_rap\": 1}")
    formatted_json.write("]}")


def compose_dataset():
    compose_unformatted_json()
    randomize_unformatted_json()
    format_json()
