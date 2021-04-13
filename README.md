# Disaster Response Pipeline Project
### Table of Contents

1. [Installation](#installation)
2. [Motivation](#motivation)
3. [File Descriptions](#files)
4. [Instructions](#Instructions)
5. [Results](#results)
6. [Licensing, Authors, and Acknowledgements](#licensing)
<p align="center">
  <img src="disaster response.png" width="600" title="hover text">
 
</p>





## Installation <a name="installation"></a>

This project uses Python 3.6, besides Jupyter Notebook. The list of libraries to run this project are:
* Pandas
* Numpy
* MatplotLib
* Sqllite
* Sqlalchemy
* Sklearn

## Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

## Motivation<a name="motivation"></a>

In every distater happens ther are are thousands of messages that are sent to orginization that are responsible to handle the situation and classification of these messages is a task that needs to be automated accuratley for the fast resposne. These messages can be calssified into different categories and each message can convey request for help becasue of different co-existence motivations. In this project, a machine learning model has been trained to automate this proccess.

## File Descriptions <a name="files"></a>

In this project `ETL` and `Machine Learning` pipelines and multioutput classification method are used 

 `data/messages.csv`:
 
 `data/categories.csv`:
 
 `model/train_classifier.py`:
 
 `data/process_data.py`:


## Results<a name="results"></a>

There is an evaluation method in classifier that expresses results of the classification by the means of `F1score`, `precision`, and `recall`.


## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Credit to AirBnB for providing the data. You can find the Licensing for the data and other descriptive information at the Kaggle link available [here](https://www.kaggle.com/airbnb/seattle). This code is free to use.
