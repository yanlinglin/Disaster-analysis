# Disaster Response Pipeline Project

## Summary of the project 
This work is part of the Udacity Data Scientist Nanodegree. This project is in cooperation with Figure Eight. In this project, we will analyze disaster data from Figure Eight to build a model for an API that classifies disaster messages.

The project is divided into three parts:

1. ETL Pipeline

- In a Python script, process_data.py, write a data cleaning pipeline that:

- Loads the messages and categories datasets
- Merges the two datasets
- Cleans the data
- Stores it in a SQLite database

2. ML Pipeline

- In a Python script, train_classifier.py, write a machine learning pipeline that:

- Loads data from the SQLite database
- Splits the dataset into training and test sets
- Builds a text processing and machine learning pipeline
- Trains and tunes a model using GridSearchCV
- Outputs results on the test set
- Exports the final model as a pickle file

3. Flask Web App

## Description of the Python scripts

notebook/: ETL Pipeline Preparation.ipynb and ML Pipeline Preparation.ipynb, which contains the ETL and ML pipelines in the Jupyter Notebooks and can be run directly.
data/: process_data.py, which contains the Python script that runs the steps above to create a database
model/: train_classifier.py, which contains the Python script that runs the steps above to create and train a ML pipeline.
app/: run.py, which contains the Python script to create a web app. 

## How to run the Python scripts

### Installation
To clone the repository, run the following command:
'''
git clone https://github.com/yanlinglin/Disaster-analysis.git
'''
### Run the code

1. Run the following commands in the project's root directory to set up the database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

(3. Go to http://0.0.0.0:3001/)

3. In a new command terminal,  type: env|grep WORK to obtain SPACEID.

4. Open a new tab, follow https://SPACEID.udacity-student-workspaces.com/ to access the web app. 
## Screenshots
![image](https://user-images.githubusercontent.com/38507020/144914736-c5506b7a-3cf1-4ff8-8f83-b6c5cc523c68.png)
![image](https://user-images.githubusercontent.com/38507020/144914752-ced751a4-6c74-4635-9580-e1f07ce11536.png)
![image](https://user-images.githubusercontent.com/38507020/144914887-d27d3971-8569-4e12-b3a3-deb38e0290ab.png)

## Acknowledgement
Thanks to Udacity for providing the starter code; thanks to Figure Eight for providing the dataset. 
