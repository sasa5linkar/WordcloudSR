# WordcloudSR

## Overview

WordcloudSR is a Python tool designed to transform Serbian texts into visually appealing word clouds and generate frequency analysis of lemmatized words. This tool leverages natural language processing with TreeTagger to analyze Serbian text, perform lemmatization, and generate both word clouds and CSV frequency reports that highlight the most frequent and significant words in the text.

## Features

- **Serbian Language Processing**: Specialized text processing and lemmatization for Serbian language texts
- **Word Cloud Generation**: Creates visually appealing word clouds from processed text
- **Lemma Frequency Analysis**: Generates CSV files with lemma frequencies for detailed text analysis
- **Stopword Filtering**: Automatically filters common stopwords to improve visualization and analysis
- **Batch Processing**: Process multiple folders of text files in a single run

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+ installed on your system
- TreeTagger installed for Serbian language support ([TreeTagger Download](https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/))
- Sufficient disk space for storing generated images and CSV files

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sasa5linkar/WordcloudSR
cd WordcloudSR
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install the Required Packages

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the root directory of the project and specify the TreeTagger path:

```
TREETAGGER_PATH = 'path/to/your/treetagger/serbian.par'
```

Replace `'path/to/your/treetagger/serbian.par'` with the actual path to your TreeTagger Serbian parameter file.

## Verify Installation

To confirm that TreeTagger is working properly:

```bash
python test.py
```

If everything is set up correctly, you should see output similar to:

```
=== Serbian TreeTagger Test ===

Initializing Serbian TreeTagger...
Testing lemmatization...
Input sentence:
  "Ovo je kratka rečenica za testiranje taggera."

Lemmatized output:
  "ovaj jesam kratak rečenica za testiranje taggera ."

Test completed successfully!
```

## Project Structure

```
WordcloudSR/
├── input/                  # Input directory for text files
│   ├── Folder1/           # Subdirectories containing text files
│   │   ├── file1.txt
│   │   └── file2.txt
│   └── Folder2/
│       ├── file3.txt
│       └── file4.txt
├── output/                 # Output directory for results
├── .env                    # Environment configuration
├── SerbianTagger.py        # TreeTagger wrapper for Serbian
├── wordcloudsr.py          # Word cloud generation script
├── wordfrqsr.py            # Word frequency analysis script
├── stopwords.txt           # Serbian stopwords list
├── test.py                 # Installation verification script
└── requirements.txt        # Project dependencies
```

## Usage

### Preparing Input Files

Place the Serbian text files you want to analyze in subdirectories of the `input` folder:

1. Create a subdirectory in the `input` folder for each set of related texts
2. Place `.txt` files (UTF-8 encoded) in these subdirectories
3. Each subdirectory will be processed as a separate collection, generating its own word cloud and frequency report

### Generating Word Clouds

To generate word clouds from your text files:

```bash
python wordcloudsr.py
```

The script processes all text files in each subdirectory of the `input` folder, lemmatizes the text, and generates word cloud images. By default, it generates word clouds with collocations (word pairs).

Two images will be created for each subdirectory in the `output` folder:
- `Subdirectory_Name.png`: Standard word cloud
- `Subdirectory_Name_collocations.png`: Word cloud with collocations

### Generating Lemma Frequency Reports

To generate CSV files with word frequency analysis:

```bash
python wordfrqsr.py
```

This script processes all text files in each subdirectory, lemmatizes the text, counts lemma frequencies, and saves the results as CSV files in the `output` folder. The CSV files will be named after the subdirectory and contain two columns:
- `Lemma`: The lemmatized word
- `Frequency`: The frequency count

### Customizing Stopwords

To customize the stopwords that should be excluded from analysis:

1. Open the `stopwords.txt` file
2. Add or remove words as needed (one word per line)
3. Save the file

## Advanced Usage

### Command-Line Arguments

Both scripts support optional command-line arguments for customization:

```bash
# Custom input/output directories and disable collocations
python wordcloudsr.py --input custom_input --output custom_output --no-collocations

# Specify different stopwords file
python wordfrqsr.py --stopwords custom_stopwords.txt
```

## Troubleshooting

### Common Issues

1. **TreeTagger Not Found**: Ensure the TREETAGGER_PATH in .env points to the correct Serbian parameter file
2. **Encoding Issues**: Make sure text files are saved with UTF-8 encoding
3. **Empty Word Clouds**: Check if your input files contain enough text or if stopwords are filtering too much content

### Logs

Both scripts generate logs that can help diagnose issues:

```bash
# View last 50 lines of logs
tail -n 50 wordcloud.log
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the license included in the repository.

## Acknowledgments

- [TreeTagger](https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/) for providing the lemmatization tool
- [WordCloud](https://github.com/amueller/word_cloud) Python library for word cloud generation

1. Place the text files that you want to process in the `input` folder. The files should be in .txt format and encoded in UTF-8.

2. Run the following command:

```bash
python wordfrqsr.py
```

The CSV files will be saved in the `output` folder. They will have the same name as the subfolders in the `input` folder.

## Contributing to WordcloudSR
To contribute to WordcloudSR, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## Contributors
Thanks to the following people who have contributed to this project:

- [@sasa5linkar](https://github.com/sasa5linkar)

## Contact
If you want to contact me, you can reach me at `sasa5linkar@gmail.com`.

## License
This project is licensed under the Creative Commons License - see the [LICENSE.md](LICENSE.md) file for details.


