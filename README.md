# Module 3 - Sprint 2 Gradient Boosted Trees 

This project is a part of the Turing College Data Science learning programme at (https://www.turingcollege.com/data-science). Projects outline can be found at the [main GitHub repo](https://github.com/TuringCollegeSubmissions/vbeino-ML.2.5.git).

#### -- Project Status: [Active]

## Project Intro/Objective
The purpose of this project is to develop and practice supervised machine learning skills as part of the Data Science programme curriculum. For the provided 'Stroke Prediction' dataset a task was provided to produce a binary machine learning classifier which would accurately predict stroke labels for patients. 

### Technologies
* Python
* Pandas, Jupyter
* Scikit-Learn
* FastAPI
* SHAP

## Project Description
For the given Stroke Prediction dataset (https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) EDA was performed, following questions answered using Chi2 hypothesis testing method:

- Is there a statistically significant relationship between the Residence type (Urban/Rural) and the presence of stroke in patients?
- Is there a statistically significant relationship between gender and the presence of a stroke in patients?

A tuned Logistic Regression model used as baseline with Average Precision score of ** on training dataset

Random Forest, XGBoost and LightGBM models assembled and tuned using RandomGridSearch cross validation method, best performing model chosen and threshold tuned for maximum F1 score. Selected threshold applied and wrapped into a sk.lego Thresholder pipeline and deployed using FastAPI. Final model feature importance and predictions analyzed and presented using SHAP library. Scores of the final binary classifier for target label on test dataset:

- Precision: 0.19
- Recall: 0.63

## Needs of this project

- Learning purposes

## Getting Started

1. Clone this repo (for help see this [tutorial](https://github.com/TuringCollegeSubmissions/vbeino-ML.2.5.git)).
2. Pip install requirements.txt
3. Run Stroke_prediction.ipynb

- Check Stroke_prediction.pdf to see full notebook report with rendered interactive plots.

## Author 

**Lead : [Vytautas Beinoravicius ]**

