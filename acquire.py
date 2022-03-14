from env import host, user, password, get_db_url
import pandas as pd 
import os

def get_telco_data(use_cache=True):
    '''
    This function takes in no arguments, uses the imported get_db_url function to establish a connection 
    with the mysql database, and uses a SQL query to retrieve telco data creating a dataframe,
    The function caches that dataframe locally as a csv file called telco.csv, it uses an if statement to use the cached csv
    instead of a fresh SQL query on future function calls. The function returns a dataframe with the telco data.
    '''
    filename = 'telco.csv'

    if os.path.isfile(filename) and use_cache:
        print('Using cached csv...')
        return pd.read_csv(filename)
    else:
        print('Retrieving data from mySQL server...')
        df = pd.read_sql('''
        SELECT * FROM customers
        JOIN contract_types USING (contract_type_id)
        JOIN payment_types USING (payment_type_id)
        JOIN internet_service_types USING (internet_service_type_id);''' , get_db_url('telco_churn'))
        print('Caching data as csv file for future use...')
        df.to_csv(filename, index=False)
        return df
