import pandas as pd

# Data for the table
data = {
    'Name': ['Joe', 'Phil', 'Dean'],
    'Target': [40, 38, 65],
    'Bonus': [46, 42, 70]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Data for the new table
data = {
    'week': ['11/6/2023', '11/6/2023', '11/6/2023', '11/13/2023', '11/13/2023', '11/13/2023',
             '11/20/2023', '11/20/2023', '11/20/2023', '11/27/2023', '11/27/2023', '11/27/2023',
             '12/4/2023', '12/4/2023', '12/4/2023'],
    'Metrics': ['Target', 'Bonus', 'Score', 'Target', 'Bonus', 'Score',
                'Target', 'Bonus', 'Score', 'Target', 'Bonus', 'Score',
                'Target', 'Bonus', 'Score'],
    'Joe': [40, 46, 33, 40, 46, 45, 40, 46, 35, None, None, None, 40, 46, 42],
    'Dean': [65, 70, 71, None, None, None, 65, 70, 68, 65, 70, 44, 65, 70, 66]
}
df2 = pd.DataFrame(data)

# Iterate over each row in df2
for i, row in df2.iterrows():
    # For each person
    for person in ['Joe', 'Dean']:
        # If the value is NaN
        if pd.isnull(row[person]):
            # If the metric is 'Score', use the 'Target' value
            if row['Metrics'] == 'Score':
                value = df.loc[df['Name'] == person, 'Target'].values[0]
            # Otherwise, check if the metric exists in df and use its value
            elif row['Metrics'] in df.columns:
                value = df.loc[df['Name'] == person, row['Metrics']].values[0]
            else:
                continue  # Skip if the metric is not in df and is not 'Score'
            # Replace the NaN value in df2
            df2.at[i, person] = value

print(df2)