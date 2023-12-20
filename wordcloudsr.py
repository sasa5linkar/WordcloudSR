import os
from wordcloud import WordCloud
from SerbainTagger import SrbTreeTagger

def process_files():
    input_dir = 'input'
    output_dir = 'output'
    tagger = SrbTreeTagger()

    for root, dirs, files in os.walk(input_dir):
        if root != input_dir:  # Skip the root input directory
            all_text = ""
            for file in files:
                if file.endswith('.txt'):
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        text = f.read()
                        all_text += text
            lemmatized_text = tagger.lemmarizer(all_text)
            wordcloud = WordCloud().generate(lemmatized_text)
            image_path = os.path.join(output_dir, f'{os.path.basename(root)}.png')
            wordcloud.to_file(image_path)

if __name__ == "__main__":
    process_files()