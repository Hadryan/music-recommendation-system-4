# Data Setup

## Getting the dataset
* Create a ```data``` folder in the same level as ```.gitignore```.
* Download the [Spotify Million Playlist Dataset](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge#acknowledgments) and put its ```data``` folder into the ```data``` folder you just created.
    * Directory tree should look like this:
    ```
    music-recommendation-system
    |   README.md
    |   .gitignore
    |
    └───data
    |   |   
    |   └───data
    |       |   mpd.slice.0-999.json
    |       |   ...
    |
    └───data_setup
        |   Data_Filter.ipynb
        |   ...
        
    ```
    * We can reorganize this later if this structure looks messy :(

## Data filtering
* Run ```Data_Filter1.1.ipynb``` to filter the data.
* Songs that occur fewer than 3 times in the entire dataset are removed.
* After song removals, playlists that end up having fewer than 10 songs or less than 30% of their original tracklist size are removed as well.
* Filtered data is saved in a folder called ```filtered_data``` under ```data```.
