from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from tables_sqlachemy.database_info import DatabaseInfo
from tables_sqlachemy.tables import Database
from tables_sqlachemy import database_info

# database = Database(name='LeBron', surname='James',
#                     birthday='2020-01-01', duties='NBA Legend',
#                     salary=44_474_988)

# engine = create_engine('sqlite:///database.db')
# Session = sessionmaker(bind=engine)
# session = Session()
# Base = declarative_base()

database = DatabaseInfo()
# database.insert_employee_data(name='LeBron', surname='James',
#                               birthday='2020-01-01', duties='NBA Legend',
#                               salary=44_474_988)

# database.insert_employee_data(name='Mike', surname='Tyson',
#                               birthday='2020-01-01', duties='Agent',
#                               salary=14_474_988)
# database.insert_employee_data(name='James', surname='Bond',
#                               birthday='2020-01-01', duties='Racer',
#                               salary=4_474_988)

# database.insert_employee_data(name='Wade', surname='Wilson',
#                               birthday='2020-01-01', duties='Superhero',
#                               salary=4_474_988)

# database.insert_employee_data(name='Bruce', surname='Wayne',
#                               birthday='2020-01-01', duties='Playboy',
#                               salary=994_474_988)

# database.insert_employee_data(name='Tony', surname='Stark',
#                               birthday='2020-01-01', duties='Comic Hero',
#                               salary=999_999_999)

# database.employee_employees()

# database.update_employee_data(employee_id=2, name='Kobe', surname='Bryant',
#                               birthday='2022-01-01', duties='NBA superstar',
#                               salary='30_453_000')

# database.update_employee_data(employee_id=4, name='Stephen', surname='Curry',
#                               birthday='2018-11-11', duties='NBA superstar',
#                               salary='48_070_014')

# database.delete_employee(name='Stephen')

# print(database.compare_employee_salary(amount_compare=31_000_000))

print(database.filtrate_employee_by_string(name='J', surname='L'))

# database.fired_employee(id=2, fire_date=datetime.strptime(
#     '2023-01-01','%Y-%m-%d'))

# database.change_employee_salary(id=1, salary=0)

# print(database.show_active_employees())

# print(database.active_employee(active='asdf'))
# print(database.show_employee_information(None))
