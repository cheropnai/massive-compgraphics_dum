#!/bin/bash
# datasetPath = "data/massive_dataset/data/"

# Get a list of languages to be used.
location=data/partitions

# echo "Languages in the dataset: $languages"

# Loop through the languages and run the main.py script for each language.
python src/main.py --task3 $location


