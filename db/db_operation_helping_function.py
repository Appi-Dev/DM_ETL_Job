import psycopg2

# Connect to PostgresSQL db and return connection
def connect_to_db(host, database, user, password, port=5432):
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        # Set auto commit to save changes without writing commit everytime after each command
        connection.set_session(autocommit=True)
        return connection
    except Exception as error:
        print("Error: Failed connection to server {}".format(error))
        return None

# Close connection to PostgressSQL server
def close_connection(connection):
    if connection:
        connection.close()
        print("Connection closed")
    
# Create db on Postgres Server
def create_db(cursor, dbname):
    try:
        # remove db if existing
        drop_db(cursor, dbname)
        cursor.execute("CREATE DATABASE {}".format(dbname))
    except Exception as error:
        print("Error: failed to create db {}".format(error))

# Drop db on Postgres Server
def drop_db(cursor, dbname):
    try:
        cursor.execute("DROP DATABASE IF EXISTS {}".format(dbname))
    except Exception as error:
        print("Error: failed to create db {}".format(error))

# Create table on Postgres db
def create_table(cursor, query):
    try:
        cursor.execute(query)
    except Exception as error:
        print("Error: failed to create table {}".format(error))

# Execute Query on table
def execute(cursor, query):
    try:
        cursor.execute(query)
        print('Query Executed Successfully')
    except Exception as error:
        print("Error: failed to execute query {}".format(error))

# Execute Query on table with data
def execute(cursor, query, data):
    try:
        cursor.execute(query, data)
        print('Query Executed Successfully')
    except Exception as error:
        print("Error: failed to execute query {}".format(error))