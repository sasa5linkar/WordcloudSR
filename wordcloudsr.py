import os
from wordcloud import WordCloud
from SerbianTagger import SrbTreeTagger

def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        stopwords = f.read().splitlines()
    return set(stopwords)

def process_files():
    input_dir = 'input'
    output_dir = 'output'
    tagger = SrbTreeTagger()
    stopwords = load_stopwords('stopwords.txt')

    for root, dirs, files in os.walk(input_dir):
        if root != input_dir:  # Skip the root input directory
            all_text = ""
            for file in files:
                if file.endswith('.txt'):
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        text = f.read()
                        all_text += text
            lemmatized_text = tagger.lemmarizer(all_text)
            wordcloud = WordCloud(stopwords=stopwords).generate(lemmatized_text)
            image_path = os.path.join(output_dir, f'{os.path.basename(root)}.png')
            wordcloud.to_file(image_path)

if __name__ == "__main__":
    process_files()