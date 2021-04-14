# Disaster Response Pipeline Project
### Table of Contents
1. [Installation](#installation)
2. [Description](#description)
3. [Instructions](#Instructions)
4. [Motivation](#motivation)
5. [File Descriptions](#files)
6. [Results](#results)
7. [Licensing, Authors, and Acknowledgements](#licensing)
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

## Project Descriptions<a name = "descriptions"></a>
The project has three componants which are:

1. **ETL Pipeline:** `process_data.py` file contain the script to create ETL pipline which:

- Loads the `messages` and `categories` datasets
- Merges the two datasets
- Cleans the data
- Stores it in a SQLite database

2. **ML Pipeline:** `train_classifier.py` file contain the script to create ML pipline which:

- Loads data from the SQLite database
- Splits the dataset into training and test sets
- Builds a text processing and machine learning pipeline
- Trains and tunes a model using GridSearchCV
- Outputs results on the test set
- Exports the final model as a pickle file

3. **Flask Web App:** the web app enables the user to enter a disaster message, and then view the categories of the message.

The web app also contains some visualizations that describe the data. 
 

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

In this project we want to implement `ETL` and `Machine Learning` pipelines to classify messages in a data set provides by figure8 besides visualization and a web interface that can classifiy user input messages.


## File Descriptions <a name="files"></a>

The files structure is arranged as below:

	- README.md: read me file
	- workspace
		- \app
			- run.py: flask file to run the app
		- \templates
			- master.html: main page of the web application 
			- go.html: result web page
		- \data
			- disaster_categories.csv: categories dataset
			- disaster_messages.csv: messages dataset
			- DisasterResponse.db: disaster response database
			- process_data.py: ETL process
		- \models
			- train_classifier.py: classification code


## Results<a name="results"></a>

There is an evaluation method in classifier that expresses results of the classification by the means of `F1 Score`, `Precision`, and `Recall`.


## Licensing, Authors, Acknowledgements<a name="licensing"></a>

This code is free to use and share.
