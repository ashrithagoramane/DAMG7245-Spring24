""" Create Database, Table, and Warehouse"""
#!/usr/bin/env python
import warnings
warnings.filterwarnings("ignore")

from sqlalchemy import create_engine

user='ashrithagoramane'
password='Ashritha123'
account_identifier='bdwmphh-uj30628'

engine = create_engine(
    'snowflake://{user}:{password}@{account_identifier}/'.format(
        user='ashrithagoramane',
        password='Ashritha123',
        account_identifier='bdwmphh-uj30628',
    )
)
create_database_query = "CREATE OR REPLACE DATABASE sf_tuts;"
create_table_query = """CREATE OR REPLACE TABLE emp_basic (
        first_name STRING ,
        last_name STRING ,
        email STRING ,
        streetaddress STRING ,
        city STRING ,
        start_date DATE
        )"""
create_warehouse = """CREATE OR REPLACE WAREHOUSE sf_tuts_wh WITH
   WAREHOUSE_SIZE='X-SMALL'
   AUTO_SUSPEND = 180
   AUTO_RESUME = TRUE
   INITIALLY_SUSPENDED=TRUE;
   """
try:
    connection = engine.connect()
    results = connection.execute(create_database_query)
    results = connection.execute(create_table_query)
    results = connection.execute(create_warehouse)
finally:
    print("Done")
    connection.close()
    engine.dispose()