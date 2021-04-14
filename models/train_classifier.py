import sys
import nltk
nltk.download(['punkt', 'wordnet'])
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sqlalchemy import create_engine
from sklearn.metrics import classification_report
from sklearn.externals import joblib
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier



def load_data(database_filepath):
    """
    load the data from a database
    
    Parameters:
    arg1 (string): database file path 
  
    Returns:
    X: message texts
    Y: categories of a message
    columns: columns in the categories
    """
    print('path','sqlite:///'+str(database_filepath))
    engine = create_engine('sqlite:///'+str(database_filepath))
    df = pd.read_sql_table('cleaned_data',engine)
    X=df['message'].values 
    Y = df.drop(['id','message','original','genre'],axis=1)
    columns=Y.columns.values
    Y=Y.values
    return X,Y,columns

def tokenize(text):
    """
    tokenize the input text
    Parameters:
    arg1 (string): input text
  
    Returns:
    List: tokenized text
  
    """
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
            clean_tok = lemmatizer.lemmatize(tok).lower().strip()
            clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    """
    build and return a pipeline.
    Here a Random forest classifier is used as the estimator of the MultiOutputClassifier.
    """
    forest = RandomForestClassifier(random_state=1)
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(estimator=forest))
    ])
    # Create Grid search parameters
    parameters = {
        'tfidf__use_idf': (True, False),
        'clf__estimator__n_estimators': [50, 60, 70]
    }
    cv = GridSearchCV(pipeline, param_grid=parameters)
    return cv


def evaluate_model(model, X_test, Y_test, category_names):
    """
    evaluate a model by F1 score, precision, and recall.
    
    Parameters:
    model: trained model
    X_test: X_test data
    Y_test: label of X_test data 
    category_names: name of different categories
    """
    y_pred=model.predict(X_test)
    for i in range(Y_test.shape[1]):
        print(category_names[i],":")
        print(classification_report(Y_test[:,i], y_pred[:,i]))
    


def save_model(model, model_filepath):
    """
    Save a model as a pickle file
    paramters:
    model: the model that we want to save
    model_filepath: path of the pickle file 
    """
    joblib.dump(model, model_filepath)
    


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        print('save path',model_filepath)
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
