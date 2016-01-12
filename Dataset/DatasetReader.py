import os
import csv


def get_dataset(dataset_name):
    current_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_path, dataset_name)

    dataset = []
    with open(full_path, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            dataset.append(row)

    return dataset
