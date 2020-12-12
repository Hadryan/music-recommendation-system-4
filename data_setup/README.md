# Data Setup

## Getting the dataset
* Run ```SpotifyPlaylist.ipynb``` to download data
    * Directory tree should look like this:
    ```
    music-recommendation-system
    |   README.md
    |   .gitignore
    |
    └───data
    |   |   
    |   └───artists
    |   |   |  artists.0-999.json
    |   |   |   ...
    |   |
    |   └───genre_playlists
    |       |   playlists.0-199.json
    |       |   ...
    |
    └───data_setup
        |   Data_Filter.ipynb
        |   ...
        
    ```
    * We can reorganize this later if this structure looks messy :(

## Data filtering
* Run ```Data_Labeling.ipynb``` to label data.
* (Todo) Songs that occur fewer than 3 times in the entire dataset are removed.
* (Todo) Songs with artists that do not have genre labels from Spotify API are removed.
* (Todo) After song removals, playlists that end up having fewer than 10 songs or less than 30% of their original tracklist size are removed as well.
* (Todo) Filtered data is saved in a folder called ```filtered_data``` under ```data```. (You may need to create the ```filtered_data``` folder first)

Todos aren't done yet
