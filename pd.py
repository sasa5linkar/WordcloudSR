#!/usr/bin/env python3
# filepath: d:\GitHub\WordcloudSR\pd.py
"""
Pandas Example Script

This script demonstrates basic pandas functionality for data manipulation,
specifically focusing on handling DataFrames and filling NaN values based on conditions.
This appears to be an example script unrelated to the main WordcloudSR project.

Author: Unknown
Date: May 21, 2025
"""

import pandas as pd
from typing import Dict, List, Any


def create_dataframes() -> tuple:
    """
    Create two example DataFrames for demonstration purposes.
    
    Returns:
        tuple: A tuple containing (base_df, weekly_df) DataFrames
    """
    # Data for the base table
    base_data = {
        'Name': ['Joe', 'Phil', 'Dean'],
        'Target': [40, 38, 65],
        'Bonus': [46, 42, 70]
    }
    base_df = pd.DataFrame(base_data)
    
    # Data for the weekly table
    weekly_data = {
        'week': ['11/6/2023', '11/6/2023', '11/6/2023', '11/13/2023', '11/13/2023', '11/13/2023',
                 '11/20/2023', '11/20/2023', '11/20/2023', '11/27/2023', '11/27/2023', '11/27/2023',
                 '12/4/2023', '12/4/2023', '12/4/2023'],
        'Metrics': ['Target', 'Bonus', 'Score', 'Target', 'Bonus', 'Score',
                    'Target', 'Bonus', 'Score', 'Target', 'Bonus', 'Score',
                    'Target', 'Bonus', 'Score'],
        'Joe': [40, 46, 33, 40, 46, 45, 40, 46, 35, None, None, None, 40, 46, 42],
        'Dean': [65, 70, 71, None, None, None, 65, 70, 68, 65, 70, 44, 65, 70, 66]
    }
    weekly_df = pd.DataFrame(weekly_data)
    
    return base_df, weekly_df


def fill_missing_values(base_df: pd.DataFrame, weekly_df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing values in the weekly DataFrame based on conditions referring to the base DataFrame.
    
    Args:
        base_df (pd.DataFrame): Reference DataFrame with base values
        weekly_df (pd.DataFrame): DataFrame with missing values to be filled
        
    Returns:
        pd.DataFrame: DataFrame with missing values filled according to rules
    """
    # Create a copy to avoid modifying the original
    filled_df = weekly_df.copy()
    
    # Iterate over each row in the weekly DataFrame
    for i, row in filled_df.iterrows():
        # For each person column
        for person in ['Joe', 'Dean']:
            # Only process if the value is NaN
            if pd.isnull(row[person]):
                # If the metric is 'Score', use the 'Target' value from the base DataFrame
                if row['Metrics'] == 'Score':
                    value = base_df.loc[base_df['Name'] == person, 'Target'].values[0]
                # Otherwise, check if the metric exists in the base DataFrame and use its value
                elif row['Metrics'] in base_df.columns:
                    value = base_df.loc[base_df['Name'] == person, row['Metrics']].values[0]
                else:
                    continue  # Skip if the metric is not in the base DataFrame and is not 'Score'
                
                # Replace the NaN value
                filled_df.at[i, person] = value
    
    return filled_df


def main():
    """Main function to demonstrate DataFrame manipulation."""
    # Create example DataFrames
    base_df, weekly_df = create_dataframes()
    
    print("Base DataFrame:")
    print(base_df)
    print("\nWeekly DataFrame (with missing values):")
    print(weekly_df)
    
    # Fill missing values
    filled_df = fill_missing_values(base_df, weekly_df)
    
    print("\nWeekly DataFrame (after filling missing values):")
    print(filled_df)


# Execute the main function when script is run directly
if __name__ == "__main__":
    main()