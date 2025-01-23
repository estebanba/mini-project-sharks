import pandas as pd

# LOAD THE DATAFRAME
def load_dataframe(url):
    df = pd.read_excel(url)
    return df

# CLEAN FUNCTIONS

def remove_null(df, column_list, value):
    """
    To remove nulls from a column, add a list of columns in the second parameter and
    then the value to be replaced with.
    """
    for col in column_list:
      df[col] = df[col].fillna(value)
      print(f"Null values in column '{col}' have been replaced with value: {value}.")
    return df[col]

# #Check for special characters in a column
# def check_char(column_data):
#   """
#   Function to check for special characters using regen. Please name one column to check for special characters
#   """
#   result = column_data.str.contains(r'[^a-zA-Z\s]', regex=True, na=False).sum()
#   table = column_data.str.contains(r'[^a-zA-Z\s]', regex=True, na=False)
#   print(f"The number of values with special characters in this column is: {result}")
#   return column_data[table].head(50)

def clean_y_n(df, column):
    df[column] = df[column].str.strip().str.upper().str.replace(r'[^a-zA-Z]', '', regex=True)
    df[column] = df[column].apply(lambda x: "N/A" if x not in ["N", "Y"] else x)
    return df

## Used for shark species
def clean_with_regex_dictionary(df, column, regex_map):
    df[column] = df[column].fillna("").apply(lambda x: x.lower())
    df[column] = df[column].str.lower().replace(regex_map, regex=True)
    return df

# FILTER FUNCTIONS
def filter_column_by_min_count(df, column, min_count):
    value_counts = df[column].value_counts()
    filter_dict = value_counts[value_counts >= min_count]
    df = df[df[column].isin(filter_dict.keys())]
    df.reset_index(inplace=True)
    return df

def filter_column_by_value(df, column, value):
    df = df[df[column] != value]
    df.reset_index(inplace=True)
    return df