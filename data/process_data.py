import sys
# import libraries
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath) 
    df = messages.merge(categories, how='inner', on=['id'])
    return df

def clean_data(df):
    categories_col = df.categories.str.split(';',expand=True)
    row = categories_col.iloc[0]
    category_colnames = row.apply(lambda x: x[0:len(x)-2])
    categories_col.columns = category_colnames
    for column in categories_col:
        # set each value to be the last character of the string
        categories_col[column]=categories_col[column].apply(lambda x: x[-1])
        # convert column from string to numeric
        categories_col[column] = categories_col[column].astype(int)
    categories_col['related'].replace(2,0,inplace=True)
    df.drop('categories',axis=1,inplace=True)
    df = pd.concat([df,categories_col],axis=1)
    df.drop_duplicates(inplace=True)
    return df

def save_data(df, database_filename):
    engine = create_engine('sqlite:///'+ database_filename)
    df.to_sql('df', engine, index=False,if_exists='replace')  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()