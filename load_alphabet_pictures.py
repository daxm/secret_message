"""
This script scrapes a website "http://printerprojects.com" and grabs all their alphabet gifs.
This site has A-Z, a-z, 0-9, &, ', -, @, -, $, !,#, %, ., +, ?, " characters.
"""

import os
import string
import urllib.request

baseurl = 'http://printerprojects.com/alphabet/elements'
colors = ['black', 'blue', 'red', 'green']
fileextension = '.gif'
pronouncuationwording = ['ampersand', 'apostrophe', 'at', 'dash', 'dollar', 'exclamation', 'number', 'percent', 'period', 'plus', 'question', 'quotation']
numbers = ['zero', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lc_letters = list(string.ascii_lowercase)
uc_letters = list(string.ascii_uppercase)


def get_and_save_image(baseurl, character, filename):
    directoryname = ''.join((os.getcwd(), '/', 'source_alphabet', '/', str(convert_to_ascii(character))))
    if not os.path.exists(directoryname):
        os.makedirs(directoryname)
    file = ''.join((directoryname, '/', filename))
    urllib.request.urlretrieve(baseurl.lower(), file)
    print("Saving %s" % file)

def convert_to_ascii(character):
    # This website uses the following words but we need to know the symbol to convert to ascii.
    if character == 'ampersand':
        character = '&'
    if character == 'apostrophe':
        character = "'"
    if character == 'at':
        character = '@'
    if character == 'dash':
        character = '-'
    if character == 'dollar':
        character = '$'
    if character == 'exclamation':
        character = '!'
    if character == 'number':
        character = '#'
    if character == 'percent':
        character = '%'
    if character == 'period':
        character = '.'
    if character == 'plus':
        character = '+'
    if character == 'question':
        character = '?'
    if character == 'quotation':
        character = '"'
    if character == 'zero':
        character = '0'
    # The rest of the characters are properly formatted.
    return ord(character)

# Main Program
for color in colors:
    for character in uc_letters + numbers + pronouncuationwording:
        filename = ''.join((character, '.gif'))
        if color == 'black':
            url = ''.join((baseurl, '/', filename))
        else:
            url = ''.join((baseurl, '/', color, filename))
        filename = ''.join((color,filename))
        get_and_save_image(url, character, filename)

    for character in lc_letters:
        filename = ''.join((character, '.gif'))
        if color == 'black':
            url = ''.join((baseurl, '/', 'lc', filename))
        else:
            url = ''.join((baseurl, '/', color, 'lc', filename))
        filename = ''.join((color,filename))
        get_and_save_image(url, character, filename)
