#!/usr/bin/env python3
# filepath: d:\GitHub\WordcloudSR\wordfrqsr.py
"""
WordFrequencySR: Serbian Text Lemma Frequency Generator

This script processes Serbian text files in the input directory,
performs lemmatization using TreeTagger, and generates CSV files
containing word frequencies sorted in descending order.

Requires:
    - SerbianTagger with TreeTagger properly installed
    - treetaggerwrapper library
    - A properly formatted stopwords file

Author: Unknown
Date: May 21, 2025
"""

import os
import csv
import collections
import logging
from pathlib import Path
from typing import Set, Dict, List, Tuple, Optional
from SerbianTagger import SrbTreeTagger
from utils import (
    load_stopwords, 
    extract_text_from_directory, 
    ensure_directory_exists,
    parse_arguments,
    logger
)

def calculate_lemma_frequencies(text: str, tagger: SrbTreeTagger, stopwords: Set[str]) -> List[Tuple[str, int]]:
    """
    Calculate lemma frequencies from text after lemmatization and stopword removal.
    
    Args:
        text (str): Input text to process.
        tagger (SrbTreeTagger): Initialized Serbian TreeTagger instance.
        stopwords (Set[str]): Set of stopwords to exclude.
        
    Returns:
        List[Tuple[str, int]]: List of (lemma, frequency) pairs sorted by frequency.
    """
    if not text:
        logger.warning("Empty text provided for lemmatization")
        return []
        
    # Lemmatize the text
    lemmatized_text = tagger.lemmatize(text)
    
    if not lemmatized_text:
        logger.warning("Lemmatization produced empty result")
        return []
    
    # Count lemma frequencies
    lemma_freq = collections.Counter(lemmatized_text.lower().split())
    
    # Remove stopwords
    for stopword in stopwords:
        if stopword in lemma_freq:
            del lemma_freq[stopword]
    
    # Sort by frequency in descending order
    return sorted(lemma_freq.items(), key=lambda x: x[1], reverse=True)


def write_frequencies_to_csv(frequencies: List[Tuple[str, int]], output_path: str) -> bool:
    """
    Write lemma frequencies to a CSV file.
    
    Args:
        frequencies (List[Tuple[str, int]]): List of (lemma, frequency) pairs.
        output_path (str): Path where the CSV file will be saved.
        
    Returns:
        bool: True if successful, False otherwise
    """
    # Create directory if it doesn't exist
    ensure_directory_exists(os.path.dirname(output_path))
    
    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Lemma', 'Frequency'])
            writer.writerows(frequencies)
        logger.info(f"Successfully wrote {len(frequencies)} lemmas to {output_path}")
        return True
    except Exception as e:
        logger.error(f"Error writing to CSV file {output_path}: {e}")
        return False


def process_directory(directory: str, tagger: SrbTreeTagger, stopwords: Set[str], 
                     output_dir: str) -> Optional[str]:
    """
    Process a single directory of text files.
    
    Args:
        directory (str): Directory containing text files.
        tagger (SrbTreeTagger): Initialized tagger instance.
        stopwords (Set[str]): Set of stopwords.
        output_dir (str): Directory to save output CSV.
        
    Returns:
        Optional[str]: Path to the output CSV file if successful, None otherwise.
    """
    logger.info(f"Processing directory: {directory}")
    
    # Get all text from the directory
    all_text = extract_text_from_directory(directory)
    
    if not all_text:
        logger.warning(f"No text content found in {directory}, skipping")
        return None
        
    # Calculate lemma frequencies
    sorted_lemmas = calculate_lemma_frequencies(all_text, tagger, stopwords)
    
    if not sorted_lemmas:
        logger.warning(f"No lemmas found in {directory}, skipping CSV generation")
        return None
        
    # Determine output CSV path and write results
    csv_path = os.path.join(output_dir, f'{os.path.basename(directory)}.csv')
    
    if write_frequencies_to_csv(sorted_lemmas, csv_path):
        return csv_path
    else:
        return None


def process_files(input_dir: str = 'input', output_dir: str = 'output', 
                  stopwords_file: str = 'stopwords.txt') -> Dict[str, str]:
    """
    Process text files in subdirectories, generate lemma frequencies, and save to CSV.
    
    Args:
        input_dir (str): Directory containing subdirectories with text files.
        output_dir (str): Directory where output CSV files will be saved.
        stopwords_file (str): File containing stopwords to exclude.
        
    Returns:
        Dict[str, str]: Dictionary mapping directory names to output CSV paths.
    """
    logger.info(f"Starting text processing with input dir: {input_dir}, output dir: {output_dir}")
    
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
            
            csv_path = process_directory(root, tagger, stopwords, output_dir)
            if csv_path:
                results[os.path.basename(root)] = csv_path
            
        processed_count = len(results)
        logger.info(f"Text processing completed successfully. Processed {processed_count} directories.")
        return results
        
    except Exception as e:
        logger.error(f"An error occurred during processing: {e}")
        raise


# Run the process_files function when the script is run directly
if __name__ == "__main__":
    args = parse_arguments()
    process_files(
        input_dir=args['input'],
        output_dir=args['output'],
        stopwords_file=args['stopwords']
    )