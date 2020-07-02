import argparse

from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
from p_reporting import m_reporting as mre


def argument_parser():
    parser = argparse.ArgumentParser(description='Select country to analyze or select all')
    parser.add_argument("-c", "--country", type=str, dest='country', required=True,
                        help="'Enter a country name or All_countries for a comprehensive report")
    parser.add_argument("-j", "--job", type=str, dest='job', required=True, help="'Enter a job title")
    args = parser.parse_args()
    return args


def main(country, job):
    data = mac.acquire()
    relevant_data = mwr.transform_data(data)
    clean_data, countries_codes = mwr.country_name_import(relevant_data)
    select_job, key_uuid = mwr.job_data(clean_data, job)
    filtered_data = mwr.job_filtering(clean_data, 'Job Title', key_uuid)
    filtered_data = man.country_filtering(filtered_data, country, countries_codes)
    result = man.analyze(filtered_data, clean_data)
    mre.reporting(result)
    print('======= Pipeline is complete. You may find the results in the folder ./data/results =======')


if __name__ == '__main__':
    arguments = argument_parser()
    print(arguments.country)
    print(arguments.job)
    main(arguments.country, arguments.job)