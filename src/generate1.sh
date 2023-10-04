# !/bin/bash

# Get a list of all languages in the dataset.
cd data/massive_dataset/data/ || exit

languages=$(ls *.jsonl)
# languages=$(ls *.jsonl | sed 's/.jsonl//g')
# echo "Languages in the dataset: $languages"

# Loop through the languages and run the main.py script for each language.
cd ../../../src || exit
for language in $languages; do
  python main.py --language $language
done
