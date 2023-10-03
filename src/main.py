import sys
import json

from language_processor import LanguageProcessor

datasetPath = 'data/massive_dataset/data'

processor = LanguageProcessor(datasetPath)

# Question 1


if __name__ == '__main__':
    language = sys.argv[1]

    processor.generate_matched_xlxs(language)

