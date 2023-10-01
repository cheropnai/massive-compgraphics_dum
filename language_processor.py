import pandas as pd
import os

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

            output_dir = 'data/matched_xlsx/'

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

        for filter in filters:
            file_filtered = file[file['partition'] == filter]
            file_filtered = file_filtered.sort_values(by='id', ascending=True)

            output_dir = 'data/partitions/'

            os.makedirs(output_dir, exist_ok=True)

            output_file_path = os.path.join(output_dir, f'{language[:2]}_{filter}.jsonl')

            file_filtered.to_json(output_file_path, orient='records', lines=True)

            print(file_filtered)
