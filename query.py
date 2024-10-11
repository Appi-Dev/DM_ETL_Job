
create_country_table_query = """
                 CREATE TABLE IF NOT EXISTS Country (
                     id NUMERIC NOT NULL,
                     name VARCHAR,
                     capital VARCHAR,
                     nationality VARCHAR,
                     PRIMARY KEY(id)
                 );
                 """

insert_in_country_table_query = """
                  INSERT INTO Country (
                     id,
                     name,
                     capital,
                     nationality
                  )
                  VALUES (%s, %s, %s, %s);
                  """

create_state_table_query = """
                 CREATE TABLE IF NOT EXISTS State (
                     id NUMERIC NOT NULL,
                     name VARCHAR,
                     country_id NUMERIC NOT NULL,
                     country_name VARCHAR,
                     PRIMARY KEY(id),
                     CONSTRAINT fk_country
                        FOREIGN KEY(country_id) 
                           REFERENCES Country(id)
                 );
                 """

insert_in_state_table_query = """
                  INSERT INTO State (
                     id,
                     name,
                     country_id,
                     country_name
                  )
                  VALUES (%s, %s, %s, %s);
                  """

create_city_table_query = """
                 CREATE TABLE IF NOT EXISTS City (
                     id NUMERIC NOT NULL,
                     name VARCHAR,
                     state_id NUMERIC NOT NULL,
                     state_name VARCHAR,
                     country_id NUMERIC NOT NULL,
                     country_name VARCHAR,
                     PRIMARY KEY(id),
                     CONSTRAINT fk_state
                        FOREIGN KEY(state_id) 
                           REFERENCES State(id),
                     CONSTRAINT fk_country
                        FOREIGN KEY(country_id) 
                        REFERENCES Country(id)
                 );
                 """

insert_in_city_table_query = """
                  INSERT INTO City (
                     id,
                     name,
                     state_id,
                     state_name,
                     country_id,
                     country_name
                  )
                  VALUES (%s, %s, %s, %s, %s, %s);
                  """