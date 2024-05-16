import pandas as pd
import numpy as np
import sympy
import statsmodels.api as sm
import matplotlib.pyplot as plt

#Path
Path = 'C:/Users/baneg/OneDrive/Desktop/Git/Python/MUDAC/Data/model/23_cors.csv'

CodePath = 'C:/Users/baneg/OneDrive/Desktop/Git/Python/MUDAC/Data/model/AgDistricts.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(Path)

keydf = pd.read_csv(CodePath)

df['County'] = df['County'].str.upper().str.strip()
keydf['County'] = keydf['County'].str.upper().str.strip()

cpart = df.groupby('County')#County,Route System,Centerline Miles,Lane Miles: is the column key here
kcpart = df.groupby('County')
#State,County,ANSI,Ag District,Ag District Code 

#I want to take the Ag District column from keydf and add it to the end of this new csv file I make below
cmiles = {}

for name,group in cpart:
    miles = group['Centerline Miles'].sum() + group['Lane Miles'].sum()
    cmiles[name] = round(miles,2)
print(cmiles)

cmiles_df = pd.DataFrame(list(cmiles.items()), columns=['County', 'Total Miles'])

# Merge cmiles_df with the Ag District information from keydf
# Assuming 'County' is the common column and it's exactly named 'County' in both DataFrames
merged_df = pd.merge(cmiles_df, keydf[['County', 'Ag District']], on='County', how='left')

# Check the merged DataFrame
print(merged_df.head())

# Save the merged DataFrame to a new CSV file
output_path = 'C:/Users/baneg/OneDrive/Desktop/Git/Python/MUDAC/Data/model/County_Total_Miles_with_AgDistrict.csv'
merged_df.to_csv(output_path, index=False)

print(f"Saved the summed miles with Ag District to {output_path}")

cmiles_counties = set(df['County'].unique())
keydf_counties = set(keydf['County'].unique())

# Find counties in cmiles_df that are not in keydf
unmatched_counties = cmiles_counties.difference(keydf_counties)
print("Unmatched Counties:", unmatched_counties)