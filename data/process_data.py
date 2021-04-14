import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """
    load message and categories data from csv files and merge them
    
    parameters:
    messages_filepath: file of mesaage.csv
    categories_filepath: file path of categories.csv
    
    return:
    df : a dataframe with merged columns
    
    """
    messages = pd.read_csv(messages_filepath)
    messages.head()
    categories = pd.read_csv(categories_filepath)
    categories.head()
    df = pd.merge(messages,categories)
    df.head()
    temp=df['categories'].str.split(';',expand=True)
    columns=str.split(df['categories'][0],';')
    clear_column_names=[columnname.split('-')[0] for columnname in columns]
    temp.columns = clear_column_names
    categories = temp
    categories.columns = clear_column_names
    for column in categories.columns:
        # set each value to be the last character of the string
        categories[column] = categories[column].str.split("-").str.get(1)
        # convert column from string to numeric
        categories[column] = pd.to_numeric(categories[column],downcast='float')
    tempdf=pd.concat([df,categories] ,axis=1)
    temp=df
    for column in categories.columns:
        tempdf.drop(tempdf[tempdf[column]>1].index,inplace=True)
   
    
    return(tempdf.drop('categories',axis=1))


def clean_data(df):
    """
    remove the duplicates from a dataframe     
    
    parameters:
    df(Dataframe): data frame 
    
    """
    df=df.drop_duplicates()
    
    return df


def save_data(df, database_filename):
    """
    save a dataframe to the database 
    
    parameteres:
    df : datafram to save
    database_filename : database path to save the dataframe
    """
    engine = create_engine('sqlite:///'+str(database_filename))
    engine.execute("DROP TABLE IF EXISTS cleaned_data")
    
    df.to_sql('cleaned_data', engine, index=False)  


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
