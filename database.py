from sqlalchemy import ReleaseSavepointClause, create_engine, Column, Integer, String

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



## This is to fetch specific id from database
def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])