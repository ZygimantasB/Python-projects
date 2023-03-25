import sqlalchemy
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, VARCHAR, INT, \
    DateTime, String, Float
from sqlalchemy.orm import declarative_base, session, sessionmaker

engine = create_engine('sqlite:///database.db')
Base = declarative_base()


class Database(Base):
    __tablename__ = 'database'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255))
    surname = Column(VARCHAR(255))
    birthday = Column(VARCHAR(255))
    duties = Column(String)
    salary = Column(Float, default=1000)
    start_at = Column(DateTime, default=datetime.now)
    fired_you = Column('fired_you', DateTime, default=None)

    def __init__(self, name, surname, birthday, duties, salary,
                 fired_you=None):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.duties = duties
        self.salary = salary

        self.fired_you = fired_you

    def __repr__(self):
        return f"{self.id} {self.name} {self.birthday} {self.duties} " \
               f"{self.salary} {self.fired_you}"


Base.metadata.create_all(engine)


# class DatabaseInfo:
#     def __init__(self, engine):
#         self.engine = engine
#         Session = sessionmaker(binbd=engine)
#         session = Session()
#         """:type: sqlalchemy.orm.Session""" #  <-- No idea
#
#     def insert_employee_data(self):
#         database = Database(name='LeBron', surname='James',
#                             birthday='2020-01-01', duties='NBA Legend',
#                             salary=44_474_988)
#         session.add(DatabaseInfo)
#         session.commit()


