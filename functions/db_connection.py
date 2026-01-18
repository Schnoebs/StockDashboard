import pyodbc
#import pandas as pd # Optional: use pandas for easy data handling

def db_connection():
    try:
        connection = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};"
                        'Server=Jacobs_PC\SQLEXPRESS;'
                        "Database=StockData;"
                        "Trusted_Connection=yes;"
                        "TrustServerCertificate=yes;")
        cursor = connection.cursor()

        # Execute a simple query
        cursor.execute('SELECT * FROM testingTable')

        # Iterate over the results
        for row in cursor:
            print(f'row = {row}')

        # Or load results into a pandas DataFrame
        # df = pd.read_sql_query('SELECT * FROM your_table_name', connection)
        # print(df.head())

        # Commit any changes (e.g., after INSERT, UPDATE)
        # connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except pyodbc.Error as ex:
        print(f"An error occurred: {ex}")
