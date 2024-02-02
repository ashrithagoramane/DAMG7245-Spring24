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
copy_stage_to_table = """COPY INTO emp_basic
  FROM @sf_tuts.public.dummy
  FILE_FORMAT = (type = csv field_optionally_enclosed_by='"')
  PATTERN = '.*employees0[1-5].csv.gz'
  ON_ERROR = 'skip_file';"""
  
try:
    connection = engine.connect()
    connection.execute("USE DATABASE sf_tuts")
    connection.execute("USE WAREHOUSE sf_tuts_wh")
    results = connection.execute(copy_stage_to_table)
finally:
    print("Done")
    connection.close()
    engine.dispose()