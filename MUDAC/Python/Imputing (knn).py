import pandas as pd
import numpy as np
import sympy
import statsmodels.api as sm
import matplotlib.pyplot as plt

#Path
impute_path = 'C:/Users/baneg/OneDrive/Desktop/Git/Python/MUDAC/Python/Imputing.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(impute_path)

cpart = df.groupby('County of County_Animals')

#`grouped` is a GroupBy object; you can iterate over it to get groups

# Initialize the KNNImputer
imputer = KNNImputer(n_neighbors=2, weights="uniform")

# Perform the imputation
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

new_csv_path = 'C:/Users/baneg/OneDrive/Desktop/Git/Python/MUDAC/Python/Imputed_Turkeys_Inventory.csv'

# Save the updated DataFrame to a new CSV file
df_imputed.to_csv(new_csv_path, index=False)

print(f"Updated DataFrame saved to '{new_csv_path}'.")