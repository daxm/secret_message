"""
Take a plain text file and generate a coded message.
"""

import os
import uuid
import shutil
import random

cwd = os.getcwd()
inputfile = ''.join((cwd, '/', 'message.txt'))
outputfolder = ''.join((cwd, '/', 'coded_message'))
source_alphabet_folder = ''.join((cwd, '/', 'source_alphabet', '/'))
char_count = 1


def encode_character(source_folder, destination_folder, count):
    source_file = ''.join((source_folder, '/', grab_random_file(source_folder)))
    filename = ''.join((str(uuid.uuid4()), '_', count, '.gif'))
    destination_file = ''.join((destination_folder, '/', filename))
    shutil.copy2(source_file, destination_file)


def grab_random_file(folder):
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    return random.choice(files)


# Clear Old Coded messages
if os.path.exists(outputfolder):
    shutil.rmtree(outputfolder)
os.makedirs(outputfolder)

# Load plain text message and encode.
with open(inputfile, 'r') as f:
    message = f.read()
    message = message.strip()
    message_list = message.split(' ')
    for word in message_list:
        characters = list(word)
        for character in characters:
            letter_folder = ''.join((source_alphabet_folder, '/', str(ord(character))))
            if not os.path.exists(letter_folder):
                # This means we don't have an ascii folder for this character.
                letter_folder = ''.join((source_alphabet_folder, '/', '0'))
            encode_character(letter_folder, outputfolder, str(char_count))
            char_count += 1
        character = ' '
        letter_folder = ''.join((source_alphabet_folder, '/', str(ord(character))))
        encode_character(letter_folder, outputfolder, str(char_count))
        char_count += 1

