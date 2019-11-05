from pathlib import Path
import sys
import json
import random
from shutil import copyfile

from prepare_artist_list import ARTIST_NAME_FILE_NAME
from constants import RAW_DATA_PATH, DATASETS_PATH, DATASETS_DIV_PERCENT, MAIN_PATH


def divide_images(divided_arts_numbers, artists):
    """
    After providing names of artists and artworks numbers for each dataset paintings are copied to proper datasets.
    """
    for dataset, art_numbers in divided_arts_numbers.items():
        for idx, artist in enumerate(artists):
            idx = str(idx)
            DATASETS_PATH.joinpath(dataset, idx).mkdir(exist_ok=True)
            for art_number in art_numbers:
                art_name = ".".join(["_".join([artist, str(art_number)]), "jpg"])
                src = RAW_DATA_PATH.joinpath(artist, art_name)
                dst = DATASETS_PATH.joinpath(dataset, idx, art_name)
                copyfile(src, dst)


def prepare_arts_numbers(total):
    """Prepares all shuffled artwork numbers that will be then choosen for datasets."""
    arts_numbers = list(range(1, 1 + total))
    random.shuffle(arts_numbers)
    return arts_numbers


def calc_data_division(artists_arts_info):
    """Calculates the amount of artworks for each dataset due to delarated percentage."""
    division_amount = {}
    total = min(artists_arts_info.values())
    arts_numbers = prepare_arts_numbers(total)

    for key, value in DATASETS_DIV_PERCENT.items():
        division_amount[key] = round(value * total)
    return division_amount, arts_numbers


def prepare_data_for_classes(artists_arts_info):
    """Prepares info about artworks numbers that will be moved to each dataset."""
    division_amount, arts_numbers = calc_data_division(artists_arts_info)

    divided_arts_numbers = {}
    for key, value in division_amount.items():
        divided_arts_numbers[key] = random.sample(arts_numbers, value)
        arts_numbers = [
            number for number in arts_numbers if number not in divided_arts_numbers[key]
        ]
    return divided_arts_numbers


def prepare_datasets_paths():
    """Prepares directories for datasets that will be used during experiments."""
    DATASETS_PATH.mkdir(exist_ok=True)
    for dataset in DATASETS_DIV_PERCENT.keys():
        DATASETS_PATH.joinpath(dataset).mkdir(exist_ok=True)


def prepare_arts_info(artists, artists_info):
    """Prepares information about amount of artworks of chosen artists."""
    info = {}
    for artist in artists:
        if artist in artists_info.keys():
            info[artist] = artists_info[artist]
        else:
            raise KeyError("We can not find provided artist.")
    return info


def main(artists=["Vincent_van_Gogh", "Pablo_Picasso"]):
    artist_info_path = MAIN_PATH.joinpath(ARTIST_NAME_FILE_NAME)
    with open(artist_info_path, "r") as f:
        artists_info = json.load(f)

    artists_arts_info = prepare_arts_info(artists, artists_info)
    prepare_datasets_paths()
    divided_arts_numbers = prepare_data_for_classes(artists_arts_info)
    divide_images(divided_arts_numbers, artists)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) == 3:
        main(artists=[sys.argv[1], sys.argv[2]])
    else:
        raise ValueError("There is too much or not enough data provided.")

