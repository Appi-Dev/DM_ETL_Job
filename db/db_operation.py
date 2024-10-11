from db.db_operation_helping_function import connect_to_db, create_db, close_connection, create_table, execute
from query import create_country_table_query, insert_in_country_table_query, create_state_table_query, insert_in_state_table_query, create_city_table_query, insert_in_city_table_query

# Database connection parameters
host = 'localhost'
default_database = 'postgres'
user = 'postgres'
password = 'Something you want'
database = 'world'

# Create database
def create_database():

    # Connect to default database
    connection = connect_to_db(host, default_database, user, password);

    if connection:
        print("Established Connection");

        # Set auto commmit
        connection.set_session(autocommit=True)

        # Get cursor using connection which is used to execute commands
        cursor = connection.cursor()

        # Create database
        create_db(cursor, database)

        # Close connection to default database 
        close_connection(connection)

        # Connect to the new database world
        connection = connect_to_db(host, database, user, password);
        # Cursor for world db to execute commands
        cursor = connection.cursor()

        return connection, cursor

# Create tables in db
def create_table_for_country_state_city(cursor):
    # Create table for country
    create_table(cursor, create_country_table_query)
    # Create table for state
    create_table(cursor, create_state_table_query)
    # Create table for city
    create_table(cursor, create_city_table_query)

# Insert data in tables
def insert_data_in_table(cursor, countries, states, cities):
    # Insert in country
    insert_country(cursor, countries)
    # Insert in state
    insert_state(cursor, states)
    # Insert in city
    insert_city(cursor, cities)
    
def insert_country(cursor, countries):
    for i, data_row in countries.iterrows():
        execute(cursor, insert_in_country_table_query, list(data_row))

def insert_state(cursor, states):
    for i, data_row in states.iterrows():
        execute(cursor, insert_in_state_table_query, list(data_row))

def insert_city(cursor, cities):
    for i, data_row in cities.iterrows():
        execute(cursor, insert_in_city_table_query, list(data_row))