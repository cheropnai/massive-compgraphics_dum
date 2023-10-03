import os

from compgraphicscat.src.language_processor import LanguageProcessor

datasetpath = '..\data\massive_dataset\data'

processor = LanguageProcessor(datasetpath)

# Question 2: 2
threeLanguages = ['en-US.jsonl', 'sw-KE.jsonl', 'de-DE.jsonl']
for language in threeLanguages:
    processor.separate_on_partition(language)

# Question 2: 3
location = "..\outputs\partitions"
processor.train_translation_json(location)