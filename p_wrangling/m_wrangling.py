import requests
from bs4 import BeautifulSoup
import re

# wrangling functions


def transform_data(data):
    relevant_data = data[['country_code', 'normalized_job_code', 'age']]
    relevant_data = relevant_data[relevant_data['normalized_job_code'].notna()]
    relevant_data.rename(columns={'age': 'Age', 'country_code': 'Country', 'normalized_job_code': 'Job Title'},
                       inplace=True)
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
    countries_codes = {codes_clean[i + 1]: codes_clean[i] for i in range(0, len(codes_clean), 2)}
    clean_data = relevant_data
    clean_data['Country'].replace(countries_codes, inplace=True)
#    print(clean_data['Country'].head())
    print(countries_codes)

    return clean_data, countries_codes


# This function finds any job you want by matching your code with official tables
def finding_job(clean_data, job_title):
    key_uuid = ''
    for code in clean_data['Job Title']:
        api_url = f'http://api.dataatwork.org/v1/jobs/' + code
        response = requests.get(api_url).json()

        if response['title'] == job_title:
            key_uuid = response['uuid']
            break

    return {key_uuid: job_title}


# Select_jobs triggers the functions and finds the uuid tied to parsed job
def job_data(clean_data, job):
    select_job = finding_job(clean_data, job)
    key_uuid = list(select_job.keys())[0]
    print(select_job)
    print(key_uuid)

    return select_job, key_uuid


# Filtering by parsed job
def job_filtering(clean_data, select_job, key_uuid):
    job_filter = clean_data['Job Title'] == key_uuid
    filtered_data = clean_data[job_filter]
    filtered_data['Job Title'].replace(select_job, inplace=True)
    print(filtered_data[['Country', 'Job Title']].head(3))

    return filtered_data
