#!/usr/bin/env python3
# filepath: d:\GitHub\WordcloudSR\SerbianTagger.py
# -*- coding: utf-8 -*-
"""
SerbianTagger: TreeTagger Wrapper for Serbian Language Processing

This module provides a wrapper for TreeTagger specifically configured for Serbian language
text processing. It handles lemmatization of Serbian text using TreeTagger's capabilities.

Created on: Fri Oct 14 14:15:57 2022
Updated on: May 21, 2025
Author: "Petalinkar Saša"
"""

import os
import logging
from typing import Optional
import treetaggerwrapper as ttpw
from dotenv import load_dotenv

# Setup logging
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Get TreeTagger path from .env file
TTPARPATH = os.getenv('TREETAGGER_PATH')
if TTPARPATH:
    logger.info(f"TreeTagger path found: {TTPARPATH}")
else:
    logger.warning("TreeTagger path not found in environment variables. Make sure to set TREETAGGER_PATH in .env file.")


class SrbTreeTagger:
    """
    A wrapper for TreeTagger with the Serbian parameter file.
    
    This class provides functionality for Serbian text lemmatization using TreeTagger.
    It requires that TreeTagger is properly installed and the path to the Serbian
    parameter file is correctly set in the TREETAGGER_PATH environment variable.
    """
    
    def __init__(self):
        """
        Initialize the TreeTagger wrapper with Serbian parameter file.
        
        Raises:
            ValueError: If TREETAGGER_PATH is not set or TreeTagger initialization fails.
        """
        if not TTPARPATH:
            raise ValueError("TREETAGGER_PATH environment variable is not set. Please check your .env file.")
        
        try:
            self._tagger = ttpw.TreeTagger(TAGPARFILE=TTPARPATH)
            logger.info("Serbian TreeTagger initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize TreeTagger: {e}")
            raise ValueError(f"TreeTagger initialization failed: {e}")

    def lemmarizer(self, text: str) -> Optional[str]:
        """
        Replace all words in a string with their lemmas using TreeTagger.

        Args:
            text (str): The string to lemmatize.

        Returns:
            Optional[str]: The lemmatized string, or None if input is None.
            
        Examples:
            >>> tagger = SrbTreeTagger()
            >>> tagger.lemmarizer("Ovo je kratka rečenica za testiranje.")
            "ovaj jesam kratak rečenica za testiranje ."
        """
        if text is None:
            return None
            
        try:
            tags = self._tagger.tag_text(text)
            tags2 = ttpw.make_tags(tags)
            
            # Build lemmatized text
            result = []
            for tag in tags2:
                if tag.__class__.__name__ == "Tag":
                    result.append(tag[2])
                    
            return " ".join(result)
            
        except IndexError as e:
            logger.error(f"Error during lemmatization: {e}")
            logger.error(f"Problematic tags: {tags2}")
            return text  # Return original text on error
            
        except Exception as e:
            logger.error(f"Unexpected error during lemmatization: {e}")
            return text  # Return original text on error
