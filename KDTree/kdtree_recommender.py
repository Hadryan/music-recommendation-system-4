import pickle
import numpy as np
from pathlib import Path
from csv import reader
import json
from random import Random, seed

class KDTreeRecommender:
    def __init__(self, path_to_tree, path_to_playlist_indices, path_to_features):
        self.tree = pickle.load(open(path_to_tree, 'rb'))
        self.playlist_indices = self._getPlaylistIndices(path_to_playlist_indices)
        self.features = self._getFeatures(path_to_features)
        self.scaled_features = self._scaleFeatures()
        self.random = Random(seed(1))
    
    def _getPlaylistIndices(self, path):
        with open(path) as f:
            data = json.load(f)
            return data
    
    def _getFeatures(self, path):
        features_folder = Path(path).glob('**/*')
        features_files = [x for x in features_folder if x.is_file()]

        track_features = []

        for f in features_files:
            with open(f, 'r') as infile:
                rd = reader(infile)
                row1 = next(rd)
                for line in rd:
                    track_features.append(line)
        
        names = [track[:2] for track in track_features]
        features = [track[2:len(track)-1] for track in track_features]
        features = np.array(features)

        new_features = []

        #Convert to float
        for track in features:
            float_array = track.astype(np.float)
            new_features.append(float_array)
        
        return names, new_features
    
    def _scaleFeatures(self, high=1.0, low=0.0):
        rawpoints = self.features[1]
        mins = np.min(rawpoints, axis=0)
        maxs = np.max(rawpoints, axis=0)
        rng = maxs - mins
        return high - (((high - low) * (maxs - rawpoints)) / rng)

        #Convert to float
        for track in features:
            float_array = track.astype(np.float)
            new_features.append(float_array)
        
        return names, new_features

    def query(self, track_index, k):
        track_input = np.reshape(self.scaled_features[track_index], newshape=(1, len(self.scaled_features[track_index])))
        return self.tree.query(track_input, k=k)

    def getNewPlaylist(self, playlist_name):
        k = 7
        playlist_indices = self.playlist_indices[playlist_name]
        new_playlist = []
        for index in playlist_indices:
            distances, indices = self.query(index, k)
            random_ind = self.random.randint(1, k-1)
            new_playlist.append(indices[0][random_ind])
        return new_playlist

    def getNames(self, playlist_indices):
        names = []
        for index in playlist_indices:
            names.append(self.features[0][index])
        return names

def main():
    path_to_tree = 'kdtree.sav'
    path_to_playlist_indices = '../data/playlist_indices.json'
    path_to_features = '../data/track_features_updated/'
    recommender = KDTreeRecommender(path_to_tree, path_to_playlist_indices, path_to_features)
    print(recommender.scaled_features[0])

    # dist, ind = tree.query(np.reshape(features[60], newshape=(1, len(features[60]))), k=6)

    # for neighbor in ind[0]:
        # print(names[neighbor])
    # print(track_lists[:5])

if __name__ == '__main__':
    main()