
# TELCO Classification Project 
### - by Kristofer Rivera

## Project Summary

### Project Objectives
- Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.
- Create modules (acquire.py, prepare.py) that make your process repeateable.
- Construct a model to predict customer churn using classification techniques.
- Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your target audience.
- Answer panel questions about your code, process, findings and key takeaways, and model.

### Deliverables
- README.md file containing the project information
- Final Report that summarizes and removes extraneous elements
- Acquire and prepare files
- CSV file with customer_id, probability of churn, and prediction of churn
- Live Presentation walking through report

## Planning

### Business Goals

- The goal of this project is to find drivers of churn at Telco and answer the question: "Why are customers churning? 
- Construct a Machine Learning classification model that can accurately predict customer churn.
- Deliver a report that clearly lays out findings and insights, and summarizes the process taken to reach them.
- Present recommendations to stakeholders.


### Initial Questions to Answer ##

- Is there a service type more associated with churn than expected?
- Is a certain payment or contract type associated with higher churn?
- Do customers who churn have higher average monthly charges?
- Do monthly charges increase with tenure? How does this affect churn?


### Minimum Viable Product
- Using exploratory analysis, find drivers of churn that can be used as features in a classification model that will predict churn at a rate greater than the baseline.

### Project Pipline

### Acquire:
- Acquire.py function brings in TELCO data from Codeup's MySQL server
- 7043 Rows (customers)
- 24 Columns (features)
- Acquire data from a mySQl database
- Clean and prep my data, dropping unnedssary and duplicate columns, encoing my variables and creating dummy variables for categorical values where necessary.
- Explore data by answering my initial questions using visualizations made through matplotlib and seaborn and conducting statistical tests
- Create machine learning models using the top features and drivers of churn discovered during exploration
- Summarize and coalesce data into a final report that includes key findings and recommendations

### Prepare:
- Created function labled prep_telco that cleaned, and prepped data, a function called split_telco that split my data and one called create_xy that created variables to be used in my modeling. Preparation included:
- Dropping Duplicates
- Removing white space
- Removing rows where tenure and total_charges = 0
- Converting 'total_charges' from obj to float
- Encoding (Changing Yes to 1 and No to 0)
- Creating dummy variables for 'gender', 'contract_type', 'payment_type', 'internet_service_type'
- Concatenating the dummy variables
- Dropping redundant columns
- Renaming columns for clarity
- Results:
  - 7043 Rows
  - 29 Columns

### Explore:
- Created a visualiztion to get an overview of each variables correlatin to churn
- Conducted statistical tets to verify statistical significance of top variables against an alpha of .05
- Created visualizations using matplotlib and seaborn to better understand top drivers and create insights

### Model:
- Calculated baseliine accuracy by assuming a mode that predicts no customers churn since that is the most common outcome
- Split my data into 3 samples: train, validate, test
- Created models fitted to training data that utilized all features including decision trees, random forests, K neighrest neighbor and logistic regression
- Created models that only utilized top 5 features
- Cretaed models that only utilized top 2 features
- Evaluated models on validate data and compared accuracy scores and other metrics to choose 3 best performing models from a total of 14
- Tested my best performing model with the least dimensionality on test data set


## Executive Summary
#### Why are our customers churning?
- They are on a monthly contract
- They use fiber optic internet	
- They pay using electronic check	vs automatic payments
- Higher monthly charges	


#### Why our customers are being retained?
- They use our online backup service	
- They pay with a mailed check	
- They pay using bank transfer
- They pay with credit card	
- They have dsl internet	
- They have a partner and/or dependents	
- They use  tech support	
- They use online security	
- They have a one or two year contract	
 	
### Can we predict churn?
- ##### Best model was a logistic regression model using all features but I belive it was overfit. The model I recommend is another logistic regression using only the top 5 drivers of churn as features. Using this model helps reduce the risk of overfitting.
- #### Using my recommended model, we can predict with 76% accuracy whether or not a customer will churn.


### Data dictionary
Target |   Description |    Data Type
--|--|--
churn |   indicates whether or not a customer churned |   int64

Categorical Features |  Description |    Data Type
--|--|--
senior_citizen |    indicates if the customer is a senior citizen |  int64
partner |    indicates if the customer has a partner | int64
dependents |        indicates if the customer has dependents |   int64
phone_service |    indicates if the customer has phone service with Telco    |  int64
multiple_lines |    indicates if the customer with phone service has multiple lines    |    int64
online_security |    indicates if the customer has online security services |   int 64
online_backup |    indicates if the customer has online backup services |   int64
device_protection |     indicates if the customer has device protection services | int64
tech_support |  indicates if the customer has tech support services |    int64
streaming_tv |    indicates if the customer has tv streaming services |    int64
streaming_movies |    indicates if the customer has movie streaming services |    int64
payment_type | indicates the type of payment method a customer is using | int64
internet_service_type |    indicates which internet service (if any) the customer has |    int64
gender |   indicates the the customers' gender identity |    uint8
contract_type |     indicates the type of contract the customer has with Telco |   int64

Continuous Features | Description | Data Type
--|--|--
monthly_charges | how much a customer pays per month in dollars|    float64
total_charges   | how much a customer has paid over the course of their tenure |    float64
tenure          | how many months the customer has been with the company|   int64

Other   | Description   | Data Type
--|--|--
customer_id |   customer id number  | object