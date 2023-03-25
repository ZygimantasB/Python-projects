import pprint

from classes.classes import WorkersDB

workers_db = WorkersDB()

# print(workers_db.show_database())
# print(workers_db.show_birth_date())
# print(workers_db.show_name_surname_responsibilities())
# print(workers_db.show_unique_values())
# pprint.pprint(workers_db.show_worker_division(division_name='Gamybos'))
# print(workers_db.show_by_name_departament(employee_name='Giedrius'))
# print(workers_db.show_employee_by_birthday(employee_birthday='860919'))
# print(workers_db.select_employee_by_surname(employee_surname='Sabutis'))
# print(workers_db.select_employee_by_division(employee_division='Gamybos'))
# print(workers_db.execute_query("""
# INSERT INTO DARBUOTOJAS(VARDAS, PAVARDĖ, ASMENS_KODAS, PAREIGOS)
# VALUES('James', 'Bond', 38803120000, 'Programuotojas');
# """))
# print(workers_db.execute_query("""SELECT * FROM DARBUOTOJAS"""))
# workers_db.execute_query("""
# UPDATE DARBUOTOJAS SET DIRBA_NUO='2022-01-01', PAREIGOS='Vadovas',
#                        SKYRIUS_ID=2, PROJEKTAS_ID=3
# WHERE VARDAS='James' AND PAVARDĖ='Bond';
# """)
# workers_db.update_employee_data(name='Wade', surname='Wilson',
#                                 identical_id=38912120000)
# print(workers_db.execute_query("""
# SELECT * FROM DARBUOTOJAS;
# """))
# workers_db.insert_data(duties='Programuotojas', start_at='2022-01-02',
#                                      division_id=2, project_id=3)

# print(workers_db.execute_query('SELECT * FROM DARBUOTOJAS'))

# print(workers_db.collect_employee_data(employee_birth_date1='38904300000',
#                                  employee_birth_date2='38912120000'))

# workers_db.insert_two_employees(employee_surname='Antanaitis',
#                                 duties='Programuotojas')

# print(workers_db.execute_query('SELECT * FROM DARBUOTOJAS'))

# workers_db.change_employee_duties(new_employee_duties='Testuotojas',
#                                   employee_surname='Antanaitis',
#                                   current_duties='Programuotojas')

# print(workers_db.execute_query('SELECT * FROM DARBUOTOJAS'))

print(workers_db.counter_duties(name_dutie='Testuotojas'))
