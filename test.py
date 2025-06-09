#!/usr/bin/env python3
# filepath: d:\GitHub\WordcloudSR\test.py
"""
TreeTagger Test Script

A simple script to test if the TreeTagger Serbian lemmatization is working properly.
This script serves as a quick verification that the TreeTagger installation
and Serbian language files are correctly configured.

Usage:
    python test.py

Expected output:
    "ovaj jesam kratak rečenica za testiranje taggera ."

Author: Unknown
Date: May 21, 2025
"""

import sys
from SerbianTagger import SrbTreeTagger

def test_lemmatization():
    """Test the Serbian TreeTagger lemmatization functionality."""
    try:
        print("Initializing Serbian TreeTagger...")
        tagger = SrbTreeTagger()
        
        print("Testing lemmatization...")
        sentence = "Ovo je kratka rečenica za testiranje taggera."
        
        print("Input sentence:")
        print(f"  \"{sentence}\"")
        
        lemmatized = tagger.lemmatize(sentence)
        
        print("\nLemmatized output:")
        print(f"  \"{lemmatized}\"")
        
        print("\nTest completed successfully!")
        return True
        
    except Exception as e:
        print(f"\nError during testing: {e}")
        print("\nPlease check your TreeTagger installation and environment configuration.")
        print("Make sure the TREETAGGER_PATH environment variable is correctly set in your .env file.")
        return False

if __name__ == "__main__":
    print("\n=== Serbian TreeTagger Test ===\n")
    success = test_lemmatization()
    sys.exit(0 if success else 1)
