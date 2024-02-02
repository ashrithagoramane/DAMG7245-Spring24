""" Create stage and upload files to stage"""

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
create_stage = """CREATE STAGE DUMMY DIRECTORY = ( ENABLE = true );"""
upload_to_stage  = """PUT file:///tmp/employees/employees0*.csv @sf_tuts.public.dummy;"""

  
try:
    connection = engine.connect()
    connection.execute("USE DATABASE sf_tuts")
    results = connection.execute(create_stage)
    results = connection.execute(upload_to_stage)
finally:
    print("Done")
    connection.close()
    engine.dispose()