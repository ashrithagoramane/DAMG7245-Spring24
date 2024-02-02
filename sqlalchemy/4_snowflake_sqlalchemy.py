#!/usr/bin/env python
import warnings
warnings.filterwarnings("ignore")

from sqlalchemy import create_engine

engine = create_engine(
    'snowflake://{user}:{password}@{account_identifier}/'.format(
        user='ashrithagoramane',
        password='Ashritha123',
        account_identifier='bdwmphh-uj30628',
    )
)
try:
    connection = engine.connect()
    results = connection.execute('select current_version()').fetchone()
    print(results[0])
finally:
    connection.close()
    engine.dispose()
