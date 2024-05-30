from sqlalchemy import create_engine, Column, Integer, String

from sqlalchemy.orm import sessionmaker

Db_connection_string = "sqlite:///jobs.db"
connect_args  = {"check_same_thread": False}

engine = create_engine(Db_connection_string, connect_args=connect_args)

with engine.connect() as conn:
  result = conn.execute("SELECT * FROM jobs")
  result_all = result.all()
  print("result.all():", type(result_all))
  ## Check this this will return a list of tuples
  ##First element will contain a record which converted into dictionary