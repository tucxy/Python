import pandas as pd
import numpy as np
import sympy
import statsmodels.api as sm
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


# Scatter plot function
def scatter(dataframe,key,color,title,label,limits): #scatterplot function

    plt.figure(figsize=(10, 6)) # gives figure size
    plt.scatter(dataframe[key[0]], dataframe[key[1]], alpha=0.6, color=color, edgecolor='k') # plt.scatter(X,Y,...) gives a scatterplot of X \times Y.
    plt.title(title)
    plt.xlabel(label[0])
    plt.ylabel(label[1])
    plt.grid(True)

    # Sets visable axis bounds
    plt.xlim(limits[0], limits[1])  # x-axis bounds
    plt.ylim(limits[0], limits[1])  # y-axis bounds

    plt.show()

#Bar plot function
def bar(dataframe,key,color,title,label,ytick): #bargraph function

    plt.figure(figsize=(10, 6))
    plt.bar(dataframe[key[0]], dataframe[key[1]], color=color, edgecolor='k')
    plt.title(title)
    plt.xlabel(label[0]) # labels x with string in key index 1
    plt.ylabel(label[1]) # labels x with string in key index 1

    # Set y-axis tick marks interval
    plt.gca().yaxis.set_major_locator(MultipleLocator(ytick))
    
    plt.show()

# Line plot function
def line(dataframe, key, color, title, label,limits, ytick):  
#line graph function
    plt.figure(figsize=(10, 6))
    plt.plot(dataframe[key[0]], dataframe[key[1]], color=color, marker='o', linestyle='-', linewidth=2)

    plt.title(title)
    plt.xlabel(label[0])
    plt.ylabel(label[1])
    plt.grid(True)

   # Sets visable axis bounds
    plt.xlim(limits[0][0], limits[0][1])  # x- axis bounds 10 (example range)

    plt.ylim(limits[1][0], limits[1][1])  # y-axis bounds

    # Set y-axis tick marks interval
    plt.gca().yaxis.set_major_locator(MultipleLocator(ytick))

    plt.show()

# Path to [online_retail.csv]
csv_path = 'C:/Users/baneg/OneDrive/Desktop/Git/Python/Machine Learning/datasets/online_retail.csv'

#translates the csv to the dataframe filetype
df = pd.read_csv(csv_path, encoding='latin1') # needed latin1
#for online_retail.csv

# Converts 'InvoiceDate' to standard datetime and cleans 'InvoiceDate' by labeling columns that don't conform to standard format with 'NaT'

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')

# Create 'Unit Price' interval bins
bins = [0, 1, 5, 10, 20, 30, 40, 50, 100, df['UnitPrice'].max()] # gives intervals

labels = ['0-1', '1-5','5-10', '10-20', '20-30', '30-40','40-50','50-100', '100+'] #to be used for the bar graph 'x' labels

df['PriceRange'] = pd.cut(df['UnitPrice'], bins=bins, labels=labels)

''' bins is a tuple of bounds for each price interval; bins = [a1,...,an] and labels = [l1,...,ln] is a tuple of strings. So I1  = [a1,a2) |-> l1 , ... , In = [an-1,an)] |-> Ln; I_k |-> l_k

 so essentially what pd.cut does is treat every row in the column specified in the first parameter as some point on R. It then finds the unique range it lies in: [ai,aj) ( for some (i,j) in R x R) from the parameter 'bins' ( or from the partition of [0,infty) defined by 'bins') and then maps it to the 'j'-th element in the 'labels' parameter. The result is that it defines a new column of data which is simply the entire column mapped to labels according the ranges of it's elements.

 therefore, df['new key'] = pd.cut(df['column'], 'bins' = bins, 'labels' = labels) is a column of labels given by the following: 

 ~:= x ~ y if x,yin I for some Iin bins
 each Iin bins which gives the equivalence class [x]_I where xin I

 the bijection from the equivalences classes given by each Iin bins to the set of labels in 'labels 

 x~ |-> I_i |-> l_i. This column is the result of the composition of X/'bins' |-> 'labels'
'''

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')

# partitions all columns of 'Quantity' by 'PriceRange' and takes the average of 'Quantity' in each partite set


avg_quantity_per_price_range = df.groupby('PriceRange')['Quantity'].mean().reset_index()
'''
First create partition by 'PriceRange' on Unit Price columns, then create two new columns: 
# Total_quantity_Sold := total number of individual products sold from each price range

# Unique_Customer_IDs := number of unique customer ID's detected buying products from each price range
'''
#print(avg_quantity_per_price_range)
grouped_df = df.groupby('PriceRange').agg(
    Total_Quantity_Sold=('Quantity', 'sum'), #sums all [quantity] via .agg 'sum'
    Unique_Customer_IDs=('CustomerID', 'nunique') #counts all [customerID] via .agg 'nunique'
).reset_index()

grouped_df['T/N'] = grouped_df['Total_Quantity_Sold'] / grouped_df['Unique_Customer_IDs'] # this is obviously a ratio

#scatter(df,['UnitPrice','Quantity'],'red','unit price vs quantity sold', ['unit price - P','quantity sold - Q'],[0,100])

#bar(avg_quantity_per_price_range,['PriceRange','Quantity'],'skyblue','unit price vs average quantity sold per transaction', ['price range','average quantity sold per transaction'],1)

#line(grouped_df, ['PriceRange', 'T/N'], 'green', 'average quantity bought per unique customer vs Price Range', ['price range', 'total quantity sold / # of unique customer IDs'],[[0,8],[0,150]],25)

'''
in summary: pd.groupby partitions the rows of a dataset according to some particular 'key' column

 groupby('PriceRange').agg(column,operator ) tells you to collect every member of [column] and perform the operation [operator] on that aggregated data? then .reset_index() is used to return the original index to the dataset you were editing. So When you partition things it seems you can identity partite sets by setting the index to [P] for each partite set. It basically mods the dataset by via the partition by default, and has you work with cosets even though you may be manipulating objects in each coset?

pd.to_datetime assumes your column is dates and times and sets it to a standardized format

pd.cut(df['key'], bins=bins, labels=labels): partitions the column ['key'] via the intervals from bin=[a1,...,an] given by [a_{i},a_{j}) for every (i,j) in n x n, and then applies the jth label in labels to every member of the interval [aj-1,aj). The expression pd.cut(df['key'], bins=bins, labels=labels) is actually the resulting mapping for every member of ['key'] according to the partite set it belongs to.
'''
#-----------------------------MathE dataset (4).csv------------------------------

'''
for online_retail.csv
#partitions via 'Student Country' then sums and counts ['Type of Answer'] in each partite set via .agg ['sum','count']. A df called correct_by_country with the country as each key or row is created wioth columns sum and count.
'''
csv_path2 = 'C:/Users/baneg/OneDrive/Desktop/Git/Python/Machine Learning/datasets/MathE dataset (4).csv'

#Creates df and cleans the dataset by removing any rows that don't conform to the standard csv format specified via ';' and encoding 'latin1'
#-------------------------correct by country--------------------------------------
df2 = pd.read_csv(csv_path2, sep=';', encoding='latin1', on_bad_lines='skip')

correct_by_country = df2.groupby('Student Country')['Type of Answer'].agg(['sum', 'count']) 
#creates new column which is sum/count*100 called 'Percentage Correct'
correct_by_country['Percentage Correct'] = (correct_by_country['sum'] / correct_by_country['count']) * 100
#print(correct_by_country)

# Plotting percentage correct

plt.figure(figsize=(8, 6))
correct_by_country['Percentage Correct'].plot(kind='bar', color='skyblue') #plots a bar graph not via explicitly defining X x Y but by directly plotting ['Percentage Correct'] whiched is indexed by partite set: country
plt.title('Percentage of Questions Answered Correctly by Country')
plt.ylabel('Percentage Correct (%)')
plt.xlabel('Country')
plt.xticks(rotation=45) #slants x axis string values
plt.tight_layout()

plt.show()
#-------------------------correct by Topic-------------------------------
correct_by_Topic = df2.groupby('Topic')['Type of Answer'].agg(['sum', 'count']) 
#creates new column which is sum/count*100 called 'Percentage Correct'
correct_by_Topic['Percentage Correct'] = (correct_by_Topic['sum'] / correct_by_Topic['count']) * 100

plt.figure(figsize=(8, 6))
correct_by_Topic['Percentage Correct'].plot(kind='bar', color='skyblue') #plots a bar graph not via explicitly defining X x Y but by directly plotting ['Percentage Correct'] whiched is indexed by partite set: country
plt.title('Percentage of Questions Answered Correctly by Question Level')
plt.ylabel('Percentage Correct (%)')
plt.xlabel('Topic')
plt.xticks(rotation=45) #slants x axis string values
plt.tight_layout()

plt.show()
