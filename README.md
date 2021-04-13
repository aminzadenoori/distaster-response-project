# Disaster Response Pipeline Project
### Table of Contents

1. [Installation](#installation)
2. [Motivation](#motivation)
3. [File Descriptions](#files)
4. [Instructions](#Instructions)
5. [Results](#results)
6. [Licensing, Authors, and Acknowledgements](#licensing)
<p align="center">
  <img src="disaster response.png" width="350" title="hover text">
 
</p>





## Installation <a name="installation"></a>

This project uses Python 3.6, besides Jupyter Notebook. The list of libraries to run this project are:
* Pandas
* Numpy
* MatplotLib
* Sqllite
* Sqlalchemy
* Sklearn

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/
# Airbnb Seattle Data Analysis

## Motivation<a name="motivation"></a>

In this project, I want to investigate the AirBnB dataset from Seattle to answer the following questions:

1.How much is the average price of different room types, property types, and neighborhoods in Seattle data and which amenities are provided by the host in more expensive listings?

2.How different features of a listing can be related to the review scores left by customers?

3.How different features can be realted to predict the price of a listing based on the data modeling results?

## File Descriptions <a name="files"></a>

There are three files in `Files` directory of this project that investigates different questions that we want to answer.

Data for this project is included in `Data` directory.


## Results<a name="results"></a>

The report of this study can be found [here](https://amin-zadenoori.medium.com/studying-the-airbnb-seattle-data-by-crisp-dm-approach-e8fc42c34c46).


## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Credit to AirBnB for providing the data. You can find the Licensing for the data and other descriptive information at the Kaggle link available [here](https://www.kaggle.com/airbnb/seattle). This code is free to use.
