import argparse
import json
from language_processor import LanguageProcessor

datasetPath = 'data/massive_dataset/data'

processor = LanguageProcessor(datasetPath)

# Question 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--language", help="The name of the language to generate files for.")
    parser.add_argument("--task2", help="The name of the language to generate files for.")
    parser.add_argument("--task3", help="The name of the language to generate files for.")
    parser.add_argument("--save", help="The name of the language to generate files for.")

    args = parser.parse_args()

    if args.language:
        processor.generate_matched_xlxs(args.language)
    elif args.task2:
        processor.separate_on_partition(args.task2)
    elif args.task3:
        processor.train_translation_json(args.task3)
    elif args.save:
        processor.save(args.save)
    else:
        print('No arguments provided.')