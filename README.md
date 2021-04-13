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

In this project `ETL` and `Machine Learning` pipelines and multioutput classification method are used and in the diagram below file desricption is shown.
`
├── app

│   ├── run.py  # Flask file that runs app

│   └── templates   

│          ├        ── go.html                      # Classification result page of web app

│                  └── master.html                  # Main page of web app    

├── data                   

│   ├── disaster_categories.csv          # Dataset including all the categories  
│   ├── disaster_messages.csv            # Dataset including all the messages
│   └── process_data.py                  # Data cleaning
├── models
│   ├── train_classifier.py              # Train ML model
│   └── classifier.pkl                   # pikkle file of model   
|   
|── requirements.txt                     # contains versions of all libraries used.
|
└── README.md
 
`

## Results<a name="results"></a>

There is an evaluation method in classifier that expresses results of the classification by the means of `F1 Score`, `Precision`, and `Recall`.


## Licensing, Authors, Acknowledgements<a name="licensing"></a>

This code is free to use and share.
