import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import json
import argparse
#from p_acquisition import m_acquisition as mac
#from p_wrangling import m_wrangling as mwr
#from p_analysis import m_analysis as man
#from p_reporting import m_reporting as mre


def argument_parser():
    parser = argparse.ArgumentParser(description = 'Select country to analyze or select all')
    parser.add_argument("-c", "--country", type=str, dest='country', required=True,
    help="'Enter a country name or press intro for a comprehensive report")
    args = parser.parse_args()
    return args


def acquire():
    data = pd.read_csv('./data/processed/glob_data.csv')
    return data




def reduced_data(data):
    relevant_data = data[['uuid', 'age', 'country_code', 'normalized_job_code']]
    return relevant_data



def country_name_import(relevant_data):
    scrap_url = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'
    html = requests.get(scrap_url).content
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find_all('td')

    # Scrap countries list and cleaning some mess
    codes = [i.text.strip() for i in table]
    pre_codes_clean = [i for i in codes if i != ""]
    codes_clean = [re.sub(r'\b[()]|[()]\b', '', code) for code in pre_codes_clean]
    codes_clean[3] = codes_clean[3].replace('EL', 'GR')
    codes_clean[55] = codes_clean[55].replace('UK', 'GB')

    # List to Dict and back replace values into the column
    countries_codes = {codes_clean[i]: codes_clean[i + 1] for i in range(0, len(codes_clean), 2)}
    clean_data = relevant_data['normalized_job_code'].replace(countries_codes)

    return clean_data, countries_codes




#This fuction finds any job you want by matching your code and the official tables
def finding_job(clean_data, job_title):
    for code in clean_data['normalized_job_code']:
        api_url = 'http://api.dataatwork.org/v1/jobs/' + code
        response = requests.get(api_url).json()

        if response['title'] == job_title:
            value = response['uuid']

    return {job_title: value}



#This function returns a single element dict
def job_data(clean_data):
    data_job = finding_job(clean_data, 'Data Scientist')
    return data_job



def job_filter(dataframe, col, value):
    filter_job = dataframe[col] == value
    filtered_data = dataframe[filter_job]
    # Insert Replace jobs names function here
    return filtered_data


#Filtering by Data Scientist


def country_filter(dataframe, col, value):
    filter_country = dataframe[col] == value
    filtered_country = dataframe[filter_country]
    return filtered_country


#At this point, you could choose Filtering by country or not. Selecting Spain. If empty, select all.
def select_country(clean_data, country, countries_codes):
    if country == '':
        return clean_data
    elif country in countries_codes:
        filtered_data = country_filter(clean_data, 'country_code', country)
        return filtered_data
    else:
        print('Error: country name not included in the database or type error')



def quantity_func(col):
    return col.value_counts()


def analyze(filtered_data):
    result = filtered_data.groupby(['country_code', 'normalized_job_code', 'age'])['normalized_job_code'].agg(quantity_func)
    return result


def reporting(result):
    return result.to_csv(f'../data/results/mvi_report.csv', index=False)


def main(country):
    data = acquire()
    relevant_data = reduced_data(data)
    clean_data, countries_codes = country_name_import(relevant_data)
    data_job = job_data(clean_data)
    filtered_data = job_filter(clean_data, 'normalized_job_code', data_job['Data Scientist'])
    filtered_data = select_country(clean_data, country, countries_codes)
    result = analyze(filtered_data)
    reporting(result)
    print('======= Pipeline is complete. You may find the results in the folder ./data/results =======')


if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments.country)