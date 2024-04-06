import pandas as pd
import numpy as np
import sympy
import statsmodels.api as sm
import matplotlib.pyplot as plt

''' each row in this csv looks like: County of County_Animals,Year of County_Animals,"CATTLE, ON FEED - INVENTORY",HOGS - INVENTORY,TURKEYS - INVENTORY'''
# Specify the path to your CSV file
impute_path = 'C:/Users/baneg/OneDrive/Desktop/Git/Python/MUDAC/Python/Imputing.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(impute_path)

cpart = df.groupby('County of County_Animals')

# `grouped` is a GroupBy object; you can iterate over it to get groups

for name, group in cpart:
    try:
        # Process each group here
        print(f"Processing County: {name}")
        
        #checks that there are non-empty rows for TURKEYS - INVENTORY in each county
        if 'TURKEYS - INVENTORY' in group.columns and not group['TURKEYS - INVENTORY'].isna().all():
            # If there are entries for turkey inventory, then use them
            valid_rows = group[~group['TURKEYS - INVENTORY'].isna()]
            X = valid_rows[['Year of County_Animals']]  
            Y = valid_rows['TURKEYS - INVENTORY']  # Dependent variable
            model = sm.OLS(Y, sm.add_constant(X)).fit()
            # isolate 'Year of county animals' for group, and indicate it as the temporary domain
            domain = sm.add_constant(group[['Year of County_Animals']])
            predictions = model.predict(domain)
            # Only replace missing values with predictions
            dc = pd.Series(predictions, index=group.index)
            
            # Update the original DataFrame
            df.loc[group.index, 'TURKEYS - INVENTORY'] = df.loc[group.index, 'TURKEYS - INVENTORY'].fillna(dc)

            print(f"Model for {name} fitted successfully.")
        else:
            print(f"No valid turkey entries for {name}. Skipping...")
    except Exception as e:
        
        print(f"An error occurred while processing {name}: {e}")

for name, group in cpart:
    print(group)

