import sqlalchemy

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:waynehatjr@localhost:3306/projects', echo=True)