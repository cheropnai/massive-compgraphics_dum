from language_processor import LanguageProcessor

DATASETPATH = 'data/massive_dataset/data'

processor = LanguageProcessor(DATASETPATH)

# Question 2: 2
threeLanguages = ['en-US.jsonl', 'sw-KE.jsonl', 'de-DE.jsonl']
for language in threeLanguages:
    processor.separate_on_partition(language)

# Question 2: 3
location = 'data/partitions/'
processor.train_translation_json(location)