#!/bin/bash
# datasetPath = "data/massive_dataset/data/"

# Get a list of languages to be used.
language1=en-US.jsonl
language2=sw-KE.jsonl
language3=de-DE.jsonl
# echo "Languages in the dataset: $languages"

# Loop through the languages and run the main.py script for each language.
python src/main.py --task2 $language1
python src/main.py --task2 $language2
python src/main.py --task2 $language3

