## Artworks classification

### 1. DATA
Data for this expirement are taken from Kaggle: https://www.kaggle.com/ikarus777/best-artworks-of-all-time

Classification will be done for two classes (two painters):
- Vincent van Gogh - post-impressionism (877 artworks);
- Pablo Picasso - cubism, surrealism (439 artworks). 

There is a huge difference in amount of artworks for this two artists, but it will be balanced during the preprocessing. 

First of all, we need to put raw data (downloaded from kaggle) in artworks_classification directory.
So path to raw data suppose to look like: .../artworks_classification/best-artworks-of-all-time/

Remember to unzip dirs inside best-artworks-of-all-time.

1. Prepare again artist list in case if something has changed in dataset:
    ```
    python prepare_artist_list.py 
    ```
2. Prepare datasets:
    ```
    python prepare_datasets.py
    ```
Before using this script there are some constants, which can be changed in file `constants.py`. 

By default data will be divided into three datasets:
- train (60%)
- test (20%)
- validation (20%)

### 2. CLASSIFICATION PIPELINE
Data classification process will be presented in `jupyter notebook`, which is saved in: `artworks_classification/data_classification`.

