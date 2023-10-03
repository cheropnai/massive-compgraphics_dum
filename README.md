# Massive Dataset Processing
The primary goal of this project is to efficiently process a [massive](https://huggingface.co/datasets/AmazonScience/massive) dataset. It focuses on the generation of language-specific files, such as 'en-xx.xlsx,' for various languages, including English (en), Swahili (sw), and German (de). Furthermore, the project involves the creation of separate JSONL files for English (en), Swahili (sw) and German (de) containing test, train, and dev data. Additionally, it aims to produce a single JSON file that encompasses translations from English to all other languages, featuring both 'id' and 'utt' data for the training sets. To ensure efficient handling of the dataset and mitigate potential memory and time complexity issues, this project avoids the use of recursive algorithms.

## Table of Contents
- [Data File](#data-file)
- [Installation](#installation)
- [Task 1 - Language Translation](#task-1---language-translation)
- [Task 2 - Working with Files](#task-2---working-with-files)
- [Data Backup and Version Control](#data-backup-and-version-control)
## Installation
To set up the Python3 development environment and install the necessary dependencies, follow these steps:

1. Clone this repository to your local machine:
```{code}
https://github.com/cheropnai/massive-compgraphics_dum/
``` 
2. Create a virtual environment (recommended):
```{code}
python3 -m venv venv
```
Activate the virtual environment:
```{code}
source venv/bin/activate
```
3. Install the required dependencies:
```{code}
pip install -r requirements.txt
```
4. Data Import
You should have already obtained the MASSIVE Dataset mentioned in the Data File. Ensure that you have this dataset, and it is accessible in your project directory.
### Task 1 - Language Translation
In this task, we will generate en-xx.xlsx files for all languages where the pivot language is English. This will be done using the id, utt, and annot_utt columns from the dataset.
To execute this task, run the following command on the terminal or GitBash Terminal in Windows:
```{code}
./src/generate1.sh
```
This script will generate separate en-xx.xlsx files for each language where English is the pivot language.

#### Flags
Flags were used in the main.py to enable script file to call the relevant function

### Task 2 - Working with Files
In this task, we will generate separate JSONL files for English (en), Swahili (sw), and German (de) for test, train, and dev data. Additionally, we will create one large JSON file showing all translations from English (en) to other languages (xx) with id and utt for all train sets.
To execute this task, run the following command on the terminal or GitBash Terminal in Windows:
```{code}
./src/generate2_2.sh
``` 
and 
```{code}
./src/generate2_3.sh
```

This script will generate the required separated JSONL files and the large JSON file with all translations.

#### Data Backup and Version Control
Upload all generated files to a Google Drive Backup Folder for safekeeping. Done by runninng the ```upload.py``` file
