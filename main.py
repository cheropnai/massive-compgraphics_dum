import sys
import json
from language_processor import LanguageProcessor

datasetPath = 'data/massive_dataset/data'

processor = LanguageProcessor(datasetPath)

# Question 1

if __name__ == '__main__':
    language = sys.argv[1]

    processor.generate_matched_xlxs(language)

# Question 2

threeLanguages = ['en-US.jsonl', 'sw-KE.jsonl', 'de-DE.jsonl']

processor.separate_on_partition()

# for language in threeLanguages:
#     separate_on_partition(language)

def train_set_translation():
    translations = []
    location = 'data/partitions/'
    train_files = ['en_train.jsonl', 'de_train.jsonl', 'sw_train.jsonl']
    try:
        en_path = os.path.join(location, train_files[0])
        de_path = os.path.join(location, train_files[1])
        sw_path = os.path.join(location, train_files[2])

        en_df = pd.read_json(en_path, lines=True)
        de_df = pd.read_json(de_path, lines=True)
        sw_df = pd.read_json(sw_path, lines=True)

        en_df = en_df[['id', 'utt']]
        de_df = de_df[['id', 'utt']]
        sw_df = sw_df[['id', 'utt']]

        merged_df = sw_df.merge(de_df, on='id')
        merged_df = merged_df.merge(en_df, on='id')

        for row in merged_df.iterrows():
            id = row[1]['id']
            en_utt = row[1]['utt']
            de_utt = row[1]['utt_y']
            sw_utt = row[1]['utt_x']

            translations.append({
                'id': id, 
                'translation': [{
                    'en_utt': en_utt,
                    'de_utt': de_utt,
                    'sw_utt': sw_utt
                }]
            })
        output_path = 'data/translated_train/'

        os.makedirs(output_path, exist_ok=True)
        output_json_file = os.path.join(output_path, 'translations.json')


        with open(output_json_file, "w", encoding='utf-8') as json_file:
            json.dump(translations,json_file, ensure_ascii=False, indent=4)

        print('Successfully merged the train sets to translations.json')

    except Exception as e:
        print(f'Error: {e}')

# train_set_translation()

