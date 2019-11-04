from pathlib import Path
import sys
import json
from constants import ARTIST_NAME_FILE_NAME, RAW_DATA_PATH


def save(data):
    with open(ARTIST_NAME_FILE_NAME, "w") as f:
        json.dump(data, f)


def add_artworks_amount(artists):
    artist_list = {}
    for artist in artists:
        artworks = 0
        artist_path = RAW_DATA_PATH.joinpath(artist)

        for element in artist_path.iterdir():
            if element.is_file() and element.name != ".DS_Store":
                artworks += 1
        artist_list[artist] = artworks
    return artist_list


def generate_artist_list():
    artworks_path = RAW_DATA_PATH
    if artworks_path.exists():
        artists = [
            str(element).split("/")[-1]
            for element in artworks_path.iterdir()
            if element.is_dir()
        ]
    return artists


if __name__ == "__main__":
    artists = generate_artist_list()
    artist_list = add_artworks_amount(artists)
    save(artist_list)
