from pathlib import Path

MAIN_PATH = Path(__file__).absolute().parent
RAW_DATA_PATH = MAIN_PATH.joinpath("best-artworks-of-all-time", "images")
DATASETS_PATH = MAIN_PATH.joinpath("data")
DATASETS_DIV_PERCENT = {"train": 0.6, "test": 0.2, "validation": 0.2}
ARTIST_NAME_FILE_NAME = "artists_list.json"
