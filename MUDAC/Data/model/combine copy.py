import pandas as pd
import numpy as np
import sympy
import statsmodels.api as sm
import matplotlib.pyplot as plt

#Path
Path = 'C:/Users/baneg/OneDrive/Desktop/Git/Python/MUDAC/Data/model/Total Miles.csv'


# Read the CSV file into a DataFrame
df = pd.read_csv(Path)

cpart = df.groupby('Ag District')
cmiles = {}

for name,group in cpart:
    miles = group['Total Miles'].sum()
    cmiles[name] = round(miles,2)
print(cmiles)

cmiles_df = pd.DataFrame(list(cmiles.items()), columns=['Ag District', 'Total Miles'])

# Specify the path for the new CSV file
output_path = 'C:/Users/baneg/OneDrive/Desktop/Git/Python/MUDAC/Data/model/Totalmiles.csv'

# Save the DataFrame to the specified CSV file
cmiles_df.to_csv(output_path, index=False)

print(f"Saved the summed miles to {output_path}")