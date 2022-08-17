from helper import get_data

import psycopg2
import pandas as pd

##################
# Getting information from the API service
##################

url_account = "https://date.nager.at/api/v3/PublicHolidays/2022/NZ"
content_data = get_data(url_account)  # getting data from API service
print(content_data)

##################
# Uploading data to postgresql database
##################

# connecting to a database
conn = psycopg2.connect(
    database="etl",
    user='etl',
    password='etl',
    host='localhost',
    port='5432'
)

print(conn)
conn.autocommit = True
cursor = conn.cursor()
# creating tables using DDL commands
cursor.execute(open("ddl.sql", "r").read())

# converting data to sql
content_data.to_sql('test', con=conn, if_exists='replace',
                    index=False)

conn.commit()  # applying the changes
cursor.close()  # closing the cursor
conn.close()  # closing the connection with database
