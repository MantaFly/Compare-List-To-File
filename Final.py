import pandas as pd
import openpyxl 

# Read in the first Excel file
df1 = pd.read_excel('BIList.xlsx')

# Read in the second Excel file
df2 = pd.read_excel('IHList.xlsx')

# List of column names to compare
columns_to_compare = ["Lastname"]

# Initialize an empty dataframe to store the dissimilarities

dissimilarities = pd.DataFrame(df1, df2)
    

# Loop through the columns to compare
#for column in columns_to_compare:
    # Compare the two dataframes and find dissimilarities
 #   temp = df2[~df2[column].isin(df1[column])].dropna()
    #dissimilarities = dissimilarities.append(temp)
for column in df1:
    # Iterating the columns values
    for m, n in columns_to_compare(df1[column], df2[column]):
        # comparing the values
        if m != n:
            # Append the results to the dataframe
            dissimilarities = dissimilarities.append({'Column Name': column}, ignore_index=True)
# Write the dissimilarities to an Excel file
dissimilarities.to_excel("results.xlsx")
