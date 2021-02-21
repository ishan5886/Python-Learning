import pandas as pd
df = pd.read_csv('data/survey_results_public.csv')
# print(df)
df.shape  #Number of rows and columns in tuple form
df.info() #Number of rows and columns and data types of them

pd.set_option('display.max_columns', 85) #Display number of columns of data frame

pd.set_option('display.max_rows', 85) #Display number of rows of data frame

df.head(10) #show only specific number of rows -here 10

# df.head(10)  #To display first 10 rows
# df.tail(10) #To display last 10 rows