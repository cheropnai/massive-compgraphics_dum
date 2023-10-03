#!/bin/bash
# datasetPath = "data/massive_dataset/data/"

# Get a list of all languages in the dataset.
languages=$(ls 'data/massive_dataset/data/')
# echo "Languages in the dataset: $languages"

# Loop through the languages and run the main.py script for each language.
cd src || exit
for language in $languages; do
  python main.py --language $language
done
