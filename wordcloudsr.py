#!/usr/bin/env python3
# filepath: d:\GitHub\WordcloudSR\wordcloudsr.py
"""
WordCloudSR: Serbian Text Word Cloud Generator

This script processes Serbian text files in the input directory,
performs lemmatization using TreeTagger, and generates word cloud images
that visually represent word frequencies in the text.

Requires:
    - SerbianTagger with TreeTagger properly installed
    - wordcloud library
    - A properly formatted stopwords file

Author: Unknown
Date: May 21, 2025
"""

import os
import argparse
from pathlib import Path
from typing import Set, Optional, Dict, List, Tuple
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from SerbianTagger import SrbTreeTagger
from utils import (
    load_stopwords, 
    extract_text_from_directory, 
    ensure_directory_exists,
    parse_arguments,
    logger
)


def generate_wordcloud(text: str, stopwords: Set[str], collocations: bool = False,
                      width: int = 1200, height: int = 800, max_words: int = 200) -> Optional[WordCloud]:
    """
    Generate a word cloud from lemmatized text.
    
    Args:
        text (str): Lemmatized text to generate word cloud from.
        stopwords (Set[str]): Set of stopwords to exclude.
        collocations (bool): Whether to include collocations (word pairs) in the word cloud.
        width (int): Width of the word cloud image.
        height (int): Height of the word cloud image.
        max_words (int): Maximum number of words to include.
        
    Returns:
        Optional[WordCloud]: Generated word cloud object or None if generation fails.
    """
    if not text:
        logger.warning("Empty text provided for word cloud generation")
        return None
        
    try:
        # Configure and generate the word cloud
        wordcloud = WordCloud(
            stopwords=stopwords,
            collocations=collocations,
            width=width,
            height=height,
            max_words=max_words,
            background_color='white',
            prefer_horizontal=0.9,
            relative_scaling=0.5,
            min_font_size=8
        ).generate(text.lower())
        
        logger.debug(f"Generated word cloud with collocations={collocations}")
        return wordcloud
    except Exception as e:
        logger.error(f"Error generating word cloud: {e}")
        return None


def save_wordcloud(wordcloud: WordCloud, output_path: str, dpi: int = 300) -> bool:
    """
    Save a word cloud image to a file.
    
    Args:
        wordcloud (WordCloud): The word cloud object to save.
        output_path (str): Path where the image will be saved.
        dpi (int): Dots per inch for the output image.
        
    Returns:
        bool: True if saving was successful, False otherwise.
    """
    # Create directory if it doesn't exist
    ensure_directory_exists(os.path.dirname(output_path))
    
    try:
        # Use matplotlib for better quality image saving
        plt.figure(figsize=(16, 10), dpi=dpi)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.savefig(output_path, dpi=dpi, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Successfully saved word cloud to {output_path}")
        return True
    except Exception as e:
        logger.error(f"Error saving word cloud to {output_path}: {e}")
        return False


def process_directory(directory: str, tagger: SrbTreeTagger, stopwords: Set[str],
                     output_dir: str, collocations: bool,
                     width: int, height: int, max_words: int) -> Tuple[Optional[str], Optional[str]]:
    """
    Process a single directory of text files to generate word clouds.
    
    Args:
        directory (str): Directory containing text files.
        tagger (SrbTreeTagger): Initialized tagger instance.
        stopwords (Set[str]): Set of stopwords.
        output_dir (str): Directory to save output images.
        collocations (bool): Whether to include collocations.
        width (int): Width of the generated word cloud image.
        height (int): Height of the generated word cloud image.
        max_words (int): Maximum number of words in the word cloud.
        
    Returns:
        Tuple[Optional[str], Optional[str]]: Paths to the standard and collocations word cloud images
    """
    logger.info(f"Processing directory: {directory}")
    
    # Get all text from the directory
    all_text = extract_text_from_directory(directory)
    
    if not all_text:
        logger.warning(f"No text content found in {directory}, skipping")
        return None, None
        
    # Lemmatize the combined text
    lemmatized_text = tagger.lemmatize(all_text)
    
    if not lemmatized_text:
        logger.warning(f"Lemmatization failed for {directory}, skipping")
        return None, None
    
    folder_name = os.path.basename(directory)
    results = []
    
    # Generate standard word cloud
    wordcloud = generate_wordcloud(
        lemmatized_text,
        stopwords,
        collocations=False,
        width=width,
        height=height,
        max_words=max_words
    )
    if wordcloud:
        std_path = os.path.join(output_dir, f'{folder_name}.png')
        if save_wordcloud(wordcloud, std_path):
            results.append(std_path)
        else:
            results.append(None)
    else:
        results.append(None)
    
    # Generate collocations word cloud if requested
    if collocations:
        wordcloud = generate_wordcloud(
            lemmatized_text,
            stopwords,
            collocations=True,
            width=width,
            height=height,
            max_words=max_words
        )
        if wordcloud:
            coll_path = os.path.join(output_dir, f'{folder_name}_collocations.png')
            if save_wordcloud(wordcloud, coll_path):
                results.append(coll_path)
            else:
                results.append(None)
        else:
            results.append(None)
    else:
        results.append(None)
    
    return tuple(results)


def process_files(collocations: bool = False,
                 input_dir: str = 'input',
                 output_dir: str = 'output',
                 stopwords_file: str = 'stopwords.txt',
                 width: int = 1200,
                 height: int = 800,
                 max_words: int = 200) -> Dict[str, Dict[str, str]]:
    """
    Process text files in subdirectories, generate word clouds, and save as images.
    
    Args:
        collocations (bool): Whether to include collocations in the word clouds.
        input_dir (str): Directory containing subdirectories with text files.
        output_dir (str): Directory where output images will be saved.
        stopwords_file (str): File containing stopwords to exclude.
        width (int): Width of the generated word clouds.
        height (int): Height of the generated word clouds.
        max_words (int): Maximum number of words in each word cloud.
        
    Returns:
        Dict[str, Dict[str, str]]: Results dictionary with paths to generated images.
    """
    logger.info(
        f"Starting word cloud generation (collocations={collocations}, "
        f"width={width}, height={height}, max_words={max_words})"
    )
    
    # Ensure output directory exists
    ensure_directory_exists(output_dir)
    results = {}
    
    try:
        # Initialize tagger and load stopwords
        logger.info("Initializing Serbian TreeTagger")
        tagger = SrbTreeTagger()
        
        logger.info(f"Loading stopwords from {stopwords_file}")
        stopwords = load_stopwords(stopwords_file)
        
        # Process each subdirectory in the input directory
        for root, dirs, files in os.walk(input_dir):
            # Skip the root input directory itself
            if root == input_dir:
                continue
            
            folder_name = os.path.basename(root)
            std_path, coll_path = process_directory(
                root,
                tagger,
                stopwords,
                output_dir,
                collocations,
                width,
                height,
                max_words
            )
            
            # Store results
            if std_path or coll_path:
                results[folder_name] = {
                    'standard': std_path,
                    'collocations': coll_path
                }
        
        processed_count = len(results)
        logger.info(f"Word cloud generation completed. Processed {processed_count} directories.")
        return results
        
    except Exception as e:
        logger.error(f"An error occurred during processing: {e}")
        raise


def main():
    """Parse arguments and run the word cloud generation process."""
    # Get command line arguments
    args = parse_arguments()

    # Run the main process
    process_files(
        collocations=not args['no_collocations'],
        input_dir=args['input'],
        output_dir=args['output'],
        stopwords_file=args['stopwords'],
        width=args['width'],
        height=args['height'],
        max_words=args['max_words']
    )


# Run the process_files function when the script is run directly
if __name__ == "__main__":
    main()
