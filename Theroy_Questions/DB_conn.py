"""
Connecting to Database using python
Need to install the database adaptors like 

psycopg2 - PostgreSQL
mySQLconnector - MYSQL

"""

import psycopg2

try:
    # establish the DB connection
    connection = psycopg2.connect(
        host="localhost",
        database="localDB",
        user="xyz",
        password="db_password",
        port="5432",
    )

    # create cursor object cursor object allows you to execute PostgreSQL commands (e.g., queries,
    # inserts, updates) within the connected database.
    cursor = connection.cursor()

    cursor.execute("SELECT version()")

    result = cursor.fetchall()  # fetchone()#fetchmany()

    for row in result:
        print(row)

except (Exception, psycopg2.DatabaseError) as error:
    print(f"Error connecting PostgreSQL databse {error}")

finally:
    if connection:
        cursor.close()
        connection.close()
