import pandas as pd
import os
import json

class LanguageProcessor:
    def __init__(self, datasetPath):
        self.datasetPath = datasetPath

    def generate_matched_xlxs(self, language):
        englishFilePath = os.path.join(self.datasetPath, 'en-US.jsonl')

        eng = pd.read_json(englishFilePath, lines=True)
        
        eng = eng[['id', 'utt', 'annot_utt']]
    
        if language == 'en-US.jsonl':
            return
        try:
            jsonl_file_path = os.path.join(self.datasetPath, language)

            df = pd.read_json(jsonl_file_path, lines=True)

            df = df[['id', 'utt', 'annot_utt']]

            joinedDf = pd.merge(eng, df, on='id')

            output_dir = 'outputs/matched_xlsx/'

            os.makedirs(output_dir, exist_ok=True)

            output_file_path = os.path.join(output_dir, f'en-{language[:2]}.xlsx')

            joinedDf.to_excel(output_file_path, index=False)

            print(f"Successfully processed {language} and generated en-{language[:2]}.xlsx")

        except Exception as e:
            print(f"Error processing {language}: {e}")

    def separate_on_partition(self, language):
        filters = ['train', 'dev', 'test']    
        filePath = os.path.join(self.datasetPath, language)
        file = pd.read_json(filePath, lines=True)
        
        try:
            for filter in filters:
                file_filtered = file[file['partition'] == filter]
                file_filtered = file_filtered.sort_values(by='id', ascending=True)

                output_dir = 'outputs/partitions/'

                os.makedirs(output_dir, exist_ok=True)

                output_file_path = os.path.join(output_dir, f'{language[:2]}_{filter}.jsonl')

                file_filtered.to_json(output_file_path, orient='records', lines=True)

            print(f'Successfully separated {language}')
        except Exception as e:
            print(f'Error: {e}')

    def train_translation_json(self, location):
        translations = []
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

