import pandas as pd
import os
import sys

datasetPath = 'data/massive_dataset/data'

englishFilePath = os.path.join(datasetPath, 'en-US.jsonl')

eng = pd.read_json(englishFilePath, lines=True)

eng = eng[['id', 'utt', 'annot_utt']]

def generate_matched_xlxs(language):
    if language == 'en-US.jsonl':
        return
    try:
        jsonl_file_path = os.path.join(datasetPath, language)

        df = pd.read_json(jsonl_file_path, lines=True)

        df = df[['id', 'utt', 'annot_utt']]

        joinedDf = pd.merge(eng, df, on='id')

        output_dir = 'data/matched_xlsx/'

        os.makedirs(output_dir, exist_ok=True)

        output_file_path = os.path.join(output_dir, f'en-{language[:2]}.xlsx')

        joinedDf.to_excel(output_file_path, index=False) 

        print(f"Successfully processed {language}")

    except Exception as e:
        print(f"Error processing {language}: {e}")

if __name__ == '__main__':
    language = sys.argv[1]

    generate_matched_xlxs(language)
