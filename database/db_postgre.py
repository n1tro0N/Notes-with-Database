from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base

# DB_URL =

engine = create_engine('postgresql://postgres:admin@localhost/new_note')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()
