from db.db_operation import create_database, create_table_for_country_state_city, insert_data_in_table
from db.db_operation_helping_function import close_connection
from read_csv import read_country_state_cities_from_csv
     
connection, cursor = create_database()

# Read CSV Data of Country, State, City
countries, states, cities = read_country_state_cities_from_csv()
print(countries.head())

# Create Country, State and Cities table
create_table_for_country_state_city(cursor)

# Insert data in above created tables
insert_data_in_table(cursor, countries, states, cities)

# Close cursor and connection on world DB
cursor.close()
close_connection(connection)

