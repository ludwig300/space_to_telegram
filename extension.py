import os
import urllib


def get_extension(urlstring):
    parsed_url = urllib.parse.urlsplit(urlstring, scheme='', allow_fragments=True)
    unquoted_filename = urllib.parse.unquote(parsed_url[2], encoding='utf-8', errors='replace')
    splited_filename = os.path.split(unquoted_filename)
    extension = os.path.splitext(splited_filename[1])
    return extension[1]