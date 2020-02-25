# lEARNING TO CLEAN DATA AND PREPARE IT

# importing the dataset
import numpy as np
import pandas as pd

#Importing the dataset
df = pd.read_csv('property data.csv')
#checking for the first five row
print (df.head())

#looking at the data
print (df['ST_NUM'])
print (df['ST_NUM'].isnull())

# making a list of the missing value
missing_values = ["n/a", "na", "--"]
df = pd.read_csv("property data.csv", na_values = missing_values)

# Looking at the NUM_BEDROOMS column
print (df['NUM_BEDROOMS'])
print (df['NUM_BEDROOMS'].isnull())

# Detecting numbers 
cnt=0
for row in df['OWN_OCCUPIED']:
    try:
        int(row)
        df.loc[cnt, 'OWN_OCCUPIED']=np.nan
    except ValueError:
        pass
    cnt+=1

# summing the missing values for each features
print (df.isnull().sum())

# To check for missing values
print (df.isnull().values.any())

# To do a total count of missing values
print (df.isnull().sum().sum())

# Replacing missing values
# Replacing missing values with numbers
df['ST_NUM'].fillna(125, inplace = True)

# For location based replacement
df.loc[2_'ST_NUM'] = 125

# Replacing with median
median = df['NUM_BEDROOMS'].median()
df['NUM_BEDROOMS'].fillna(median, inplace = True)

# checking for the column names
column_names =df.columns
print(column_names)

# Get the Column type
df.dtypes

# Checking if the column is unique
for i in column_names:
    print('{} is unique: {}'.format(i, df[i].is_unique))

# Checking for the index value
df.index.values
 
# Checking if an index exists
'foo' in df.index.values

# Checking if index does not exist
df.set_index('PID', inplace = True)

# Creating a list comprehension of columns to lose
columns_to_drop = [column_names[i] for i in [1,3,5]]

# Drop Unwanted Columns
df.drop(columns_to_drop, inplace=True, axis = 1)



















