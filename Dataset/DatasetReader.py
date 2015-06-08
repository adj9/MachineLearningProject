__author__ = 'nzarrilli'

import os


def get_dataset(dataset_name):
    current_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_path, dataset_name)
    return open(full_path, 'r')
