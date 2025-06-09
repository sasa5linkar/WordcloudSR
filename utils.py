#!/usr/bin/env python3
# filepath: d:\GitHub\WordcloudSR\utils.py
"""
WordcloudSR Utilities

This module provides shared utility functions for the WordcloudSR project.
It contains common functionality used by both wordcloudsr.py and wordfrqsr.py.

Author: Unknown
Date: May 21, 2025
"""

import os
import logging
from typing import Set, List, Dict, Any, Optional
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='wordcloud.log',
    filemode='a'
)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s: %(message)s')
console_handler.setFormatter(formatter)
logging.getLogger('').addHandler(console_handler)

logger = logging.getLogger(__name__)


def load_stopwords(file_path: str) -> Set[str]:
    """
    Load stopwords from a specified file.
    
    Args:
        file_path (str): Path to the stopwords file.
        
    Returns:
        Set[str]: A set of stopwords for efficient lookup.
        
    Raises:
        FileNotFoundError: If the stopwords file doesn't exist.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            stopwords = f.read().splitlines()
        logger.info(f"Loaded {len(stopwords)} stopwords from {file_path}")
        return set(stopwords)
    except FileNotFoundError:
        logger.error(f"Stopwords file not found: {file_path}")
        raise


def extract_text_from_directory(directory_path: str) -> str:
    """
    Extract and combine text from all .txt files in a directory.
    
    Args:
        directory_path (str): Path to the directory containing text files.
        
    Returns:
        str: Combined text from all .txt files.
    """
    all_text = ""
    file_count = 0
    
    # Iterate over all files in the directory
    for file in os.listdir(directory_path):
        if file.endswith('.txt'):
            file_path = os.path.join(directory_path, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                    all_text += text + " "  # Add a space between files
                    file_count += 1
            except Exception as e:
                logger.warning(f"Could not read file {file_path}: {e}")
    
    logger.info(f"Processed {file_count} text files from {directory_path}")
    return all_text.strip()


def ensure_directory_exists(dir_path: str) -> None:
    """
    Ensure that a directory exists, creating it if necessary.
    
    Args:
        dir_path (str): Path to the directory to check/create.
    """
    try:
        os.makedirs(dir_path, exist_ok=True)
        logger.debug(f"Ensured directory exists: {dir_path}")
    except Exception as e:
        logger.error(f"Failed to create directory {dir_path}: {e}")
        raise


def parse_arguments() -> Dict[str, Any]:
    """
    Parse command-line arguments for WordcloudSR scripts.
    
    Returns:
        Dict[str, Any]: Dictionary containing parsed arguments.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='WordcloudSR - Serbian Text Analysis Tools')
    
    parser.add_argument('--input', default='input',
                        help='Input directory containing text files (default: input)')
    
    parser.add_argument('--output', default='output',
                        help='Output directory for results (default: output)')
    
    parser.add_argument('--stopwords', default='stopwords.txt',
                        help='Stopwords file path (default: stopwords.txt)')

    parser.add_argument('--width', type=int, default=1200,
                        help='Width of the generated word clouds (default: 1200)')
    parser.add_argument('--height', type=int, default=800,
                        help='Height of the generated word clouds (default: 800)')
    parser.add_argument('--max-words', type=int, default=200,
                        help='Maximum number of words in the word cloud (default: 200)')

    parser.add_argument('--debug', action='store_true',
                        help='Enable debug logging')
    
    args = parser.parse_args()
    
    # Set logging level based on debug flag
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        console_handler.setLevel(logging.DEBUG)
        logger.debug("Debug logging enabled")
    
    return vars(args)
