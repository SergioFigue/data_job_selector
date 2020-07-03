import pandas as pd

# analysis functions


def country_filter(dataframe, col, value):
    filter_country = dataframe[col] == value
    filtered_country = dataframe[filter_country]
    return filtered_country


# At this point, you could choose Filtering by country or not. ie Spain. If empty, selects all.
def country_filtering(filtered_data, country, countries_codes):
    print(country)
    if country == 'All_countries':
        return filtered_data
    elif country in countries_codes.values():
        filtered_data = country_filter(filtered_data, 'Country', country)
        return filtered_data.head()
    else:
        print('Error: country name not included in the database or type error')


# Find out how popular is selected job.
def analyze(filtered_data, clean_data):
    filtered_data['Quantity'] = filtered_data.groupby(['Country', 'Job Title', 'Age'])['Job Title'].transform('count')
    filtered_data['Percentage'] = (filtered_data['Quantity'] / len(clean_data)).astype(float).map(lambda n: '{:.2%}'.format(n))

    result = filtered_data
    print(result.info())
    print(result.head(50))
    return result

