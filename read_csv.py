import pandas as pd

# Read csv files of country, state and cities and return 
def read_country_state_cities_from_csv():
    countries = pd.read_csv("csv/countries.csv")
    countries_clean = countries[['id', 'name', 'capital', 'nationality']]
    print(countries_clean.head())

    states = pd.read_csv("csv/states.csv")
    states_clean = states[['id', 'name', 'country_id', 'country_name']]
    print(states_clean.head())

    cities = pd.read_csv("csv/cities.csv")
    cities_clean = cities[['id', 'name', 'state_id', 'state_name', 'country_id', 'country_name']]
    print(cities_clean.head())

    return countries_clean, states_clean, cities_clean

