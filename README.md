# WordcloudSR

## Overview
WordcloudSR is a Python tool designed to transform Serbian texts into visually appealing word clouds. This tool leverages the power of natural language processing to analyze Serbian text, perform lemmatization, and generate word clouds that highlight the most frequent and significant words in the text.

## Features
- Text processing and lemmatization for Serbian language.
- Generation of word clouds from processed text.
- Customizable word cloud appearance.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your system.
- TreeTagger installed for Serbian language support. [TreeTagger Installation Guide](#)

## Installation
### Clone the Repository
```bash
git clone https://github.com/yourusername/WordcloudSR.git
cd WordcloudSR
'''
### Set Up a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install the Required Packages

```bash
pip install -r requirements.txt
```

### Environment Configuration
Create a .env file in the root directory of the project and specify the TreeTagger path:

```bash
TREETAGGER_PATH = 'path/to/your/treetagger'
```
## Test if Treetagger works properly
```bash
python test.py
```

It shoudl return the followin:
```bash
ovaj jesam kratak rečenica za testiranje taggera
```

## Usage
To use WordcloudSR, follow these steps:

Place files that you want to process in the `input` folder. The files should be in .txt format and encoded in UTF-8. Then, run the following command, if you plant to amke more then one wordcloud you can place files in subfolders of `input` folder. 

```bash
python wordcloudsr.py
```
The images will be saved in the `output` folder. Thay will have same name as subfolders in `input` folder. Text files in input folder will be procesesed and images will be saved under name `wordcloud` in `output` folder.


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

- [@yourusername](https://github.com/yourusername)

## Contact
If you want to contact me, you can reach me at `sasa5linkar@gmail.com`.

## License
This project is licensed under the Creative Commons License - see the [LICENSE.md](LICENSE.md) file for details.


