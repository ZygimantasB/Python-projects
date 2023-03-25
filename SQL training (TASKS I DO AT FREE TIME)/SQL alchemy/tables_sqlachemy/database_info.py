from sqlalchemy import create_engine, desc, and_, or_
from sqlalchemy.orm import sessionmaker, session

from tables_sqlachemy.tables import Database


class DatabaseInfo:
    def __init__(self):
        self.engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def insert_employee_data(self, name, surname, birthday, duties,
                             salary=1000):
        database = Database(name=name, surname=surname,
                            birthday=birthday, duties=duties,
                            salary=salary)
        self.session.add(database)
        self.session.commit()

    def employee_employees(self):
        delete_last_employee = self.session.query(Database).order_by\
            (Database.id.desc()).first()

        self.session.delete(delete_last_employee)
        self.session.commit()

    def fired_employee(self, id, fire_date):
        employee = self.session.query(Database).get(id)
        employee.fired_you = fire_date
        self.session.commit()

    def change_employee_salary(self, id, salary):
        employee = self.session.query(Database).get(id)
        employee.salary = salary
        self.session.commit()



    def update_employee_data(self, employee_id, name, surname, birthday,
                             duties,
                             salary=1000):
        employee = self.session.query(Database).filter(
            Database.id == employee_id).first()
        employee.name = name
        employee.surname = surname
        employee.birthday = birthday
        employee.duties = duties
        employee.salary = salary
        self.session.commit()

    def delete_employee(self, name):
        employee = self.session.query(Database).filter_by(name=name).one()
        employee.name = name
        self.session.delete(employee)
        self.session.commit()

    def active_employee(self, active: bool):
        if active:
            action = 'Database.fired_you.is_(None)'
        else:
            action = 'Database.fired_you.is_not(None)'
        search = self.session.query(Database).filter(eval(action))
        return tuple([e for e in search])

    # def show_active_employees(self, checking_status=None):
    #     employees = self.session.query(Database).filter(or_(
    #         Database.fired_you != 'fired',
    #         Database.fired_you == checking_status
    #     )).all()
    #     result = []
    #     for employee in employees:
    #         result.append(employee)
    #
    #     return tuple(result)


    # def show_employee_information(self, checking_status):
    #     employees = self.session.query(Database).filter(or_(
    #         Database.fired_you != 'active',
    #         Database.fired_you == checking_status
    #     )).all()
    #
    #     print("ID\tName\tStatus")
    #     for employee in employees:
    #         status = 'Active' if employee.fired_you == 'active' else 'Inactive'
    #         return f"{employee.id}\t{employee.name}\t{status}"

    def compare_employee_salary(self, amount_compare):
        employee = self.session.query(Database).filter(
            Database.salary > amount_compare)
        return [salary for salary in employee]

    def filtrate_employee_by_string(self, name, surname):
        employee = self.session.query(Database).filter(or_(
            Database.name.like(f'%{name}%'),
            Database.surname.like(f'%{surname}%')
        ))
        employee.name = name
        # employee.surname = surname
        return [full_name for full_name in employee]












