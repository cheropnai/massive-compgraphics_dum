import argparse
from language_processor import LanguageProcessor

datasetPath = '../data/massive_dataset/data'

processor = LanguageProcessor(datasetPath)

# Question 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--language", help="Use this flag to run question 1")
    parser.add_argument("--task2", help="Use this flag to run question 2 part 1")
    parser.add_argument("--task3", help="Use this flag to run question 2 part 2")

    args = parser.parse_args()

    if args.language:
        processor.generate_matched_xlxs(args.language)
    elif args.task2:
        processor.separate_on_partition(args.task2)
    elif args.task3:
        processor.train_translation_json(args.task3)
    else:
        print('Invalid flag provided.')