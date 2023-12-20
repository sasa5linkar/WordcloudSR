import os
from wordcloud import WordCloud
from SerbianTagger import SrbTreeTagger

# Function to load stopwords from a file
def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        stopwords = f.read().splitlines()
    return set(stopwords)  # Return a set of stopwords

# Function to process files and generate word clouds
def process_files():
    input_dir = 'input'  # Input directory
    output_dir = 'output'  # Output directory
    tagger = SrbTreeTagger()  # Initialize tagger
    stopwords = load_stopwords('stopwords.txt')  # Load stopwords

    # Walk through all subdirectories of the input directory
    for root, dirs, files in os.walk(input_dir):
        if root != input_dir:  # Skip the root input directory
            all_text = ""  # Initialize a string to hold all text
            # Iterate over all files in the current directory
            for file in files:
                if file.endswith('.txt'):  # Process only .txt files
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        text = f.read()  # Read the file content
                        all_text += text  # Add the text to all_text
            # Lemmatize the combined text
            lemmatized_text = tagger.lemmarizer(all_text)
            # Generate a word cloud from the lemmatized text
            wordcloud = WordCloud(stopwords=stopwords).generate(lemmatized_text)
            # Determine the path for the output image
            image_path = os.path.join(output_dir, f'{os.path.basename(root)}.png')
            # Save the word cloud as an image
            wordcloud.to_file(image_path)

# Run the process_files function when the script is run directly
if __name__ == "__main__":
    process_files()