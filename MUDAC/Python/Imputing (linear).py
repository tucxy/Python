import pandas as pd
import numpy as np
import sympy
import statsmodels.api as sm
import matplotlib.pyplot as plt

#Path
impute_path = 'C:/Users/baneg/OneDrive/Desktop/Git/Python/MUDAC/Python/Imputing.csv'

df = pd.read_csv(impute_path)

cpart = df.groupby('County of County_Animals')

slopes = {}
# `grouped` is a GroupBy object; you can iterate over it to get groups
def impute(name,group,rng):
        try:
            # Process each group here
            print(f"Processing County: {name}")
            
            #checks that there are non-empty rows for TURKEYS - INVENTORY in each county
            if rng in group.columns and not group[rng].isna().all():
                # If there are entries for turkey inventory, then use them
                valid_rows = group[~group[rng].isna()]
                X = valid_rows[['Year of County_Animals']]  
                Y = valid_rows[rng]  # Dependent variable
                model = sm.OLS(Y, sm.add_constant(X)).fit()
                m = model.params['Year of County_Animals']
                slopes[name] = round(m,2)
                # isolate 'Year of county animals' for group, and indicate it as the temporary domain
                domain = sm.add_constant(group[['Year of County_Animals']])
                range = round(model.predict(domain),2)
                # replace N/A with points per county
                dc = pd.Series(range, index=group.index)
                
                # Update the original DataFrame
                df.loc[group.index, rng] = df.loc[group.index, rng].fillna(dc)

                print(f"Model for {name} fitted successfully.")
            else:
                print(f"No valid turkey entries for {name}. Skipping...")
        except Exception as e:
            
            print(f"An error occurred while processing {name}: {e}")

for name,group in cpart:
     impute(name,group,'TURKEYS - INVENTORY')
for name,group in cpart:
     impute(name,group,'HOGS - INVENTORY')
for name,group in cpart:
     impute(name,group,'CATTLE, ON FEED - INVENTORY')



new_csv_path = 'C:/Users/baneg/OneDrive/Desktop/Git/Python/MUDAC/Python/Imputed_Turkeys_Inventory.csv'

# Save the updated DataFrame to a new CSV file
df.to_csv(new_csv_path, index=False)

print(f"Updated DataFrame saved to '{new_csv_path}'.")