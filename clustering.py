import numpy as np
import pandas as pd
import json

with open('vectors.json', 'r') as fp:
    vectors = json.load(fp)vectors = pd.DataFrame.from_dict(vectors, orient = 'index')
permalinks = vectors.iloc[:, 0]
arrays = np.array(vectors.iloc[:, 1])

def closest_sweaters(sweater_vector, n=5):
    """
    Takes a sweater_vector, which is an output through the current model of a user-input picture.
    Optionally takes an argument for the number of closest permalinks to return; default 5.
    Requires the current sweaterspace vectors to be present as a dictionary in the text file 'vectors.txt'
    Returns a list of permalinks in order of decreasing similarity
    """

    distances = np.sum((arrays - sweater_vector)**2, axis = 1)
    dist_idx = np.argsort(distances)
    # Permalinks to return
    patterns_list = []
    # Counter for stepping through dist_idx
    dist_step = 0
    while len(patterns_list) < n:
        # Closest unexamined sweater
        current_image = permalinks[dist_idx[dist_step]][:-4]
        if current_image not in patterns_list:
            patterns_list.append(current_image)
        dist_step += 1
    return patterns_list
