import sqlite3

class WorkersDB:
    def __init__(self):
        self.connect = sqlite3.connect('darbuotojai.db')
        self.cursor = self.connect.cursor()

    #1. Išrinkite visus duomenis iš lentelės “DARBUOTOJAI”
    def delete_all_date(self):
        with self.connect:
            self.cursor.execute("""DROP TABLE darbuotojai""")

    #2. Išrinkite visus duomenis iš stulpelio “GIMIMO_DATA” - lentelėje “DARBUOTOJAS”.
    def show_birth_date(self):
        with self.connect:
            self.cursor.execute("""SELECT ASMENS_KODAS FROM DARBUOTOJAS""")
            return self.cursor.fetchall()

    # 3. Išrinkite visus duomenis iš stulpelių “VARDAS”,”PAVARDĖ”, “PAREIGOS” - lentelėje “DARBUOTOJAI”.
    def show_name_surname_responsibilities(self):
        credentials_list = []
        with self.connect:
            self.cursor.execute("""SELECT VARDAS, PAVARDĖ, PAREIGOS FROM DARBUOTOJAS""")
            result = self.cursor.fetchall()
            return result

    # 4. Išrinkite skirtingas reikšmes iš stulpelio SKYRIUS_PAVADINIMAS - lentelėje “DARBUOTOJAI”.
    def show_unique_values(self):
        with self.connect:
            self.cursor.execute('''
            SELECT DISTINCT(DARBUOTOJAS.SKYRIUS_ID), SKYRIUS.PAVADINIMAS
            FROM DARBUOTOJAS
            JOIN SKYRIUS ON SKYRIUS.ID = DARBUOTOJAS.SKYRIUS_ID
            ''')
            return self.cursor.fetchall()
    # 5. Išrinkite visus duomenis apie darbuotojus, kurie dirba Gamybos skyriuje.
    def show_worker_division(self, division_name):
        with self.connect:
            self.cursor.execute(f"""
            SELECT VARDAS, PAVARDĖ, PAVADINIMAS FROM DARBUOTOJAS
            JOIN SKYRIUS ON SKYRIUS.ID = DARBUOTOJAS.SKYRIUS_ID
            WHERE SKYRIUS.PAVADINIMAS LIKE '%{division_name}%';
            """)
            return self.cursor.fetchall()
    # 6. Išrinkite duomenis, kokias pareigas užima Giedrius

    def show_by_name_departament(self, employee_name):
        with self.connect:
            self.cursor.execute(f"""
            SELECT VARDAS, PAVARDĖ, PAVADINIMAS FROM DARBUOTOJAS
            JOIN SKYRIUS ON SKYRIUS.ID = DARBUOTOJAS.SKYRIUS_ID
            WHERE VARDAS LIKE '%{employee_name}%';
            """)
            return self.cursor.fetchall()

    # 7.Išrinkite visus duomenis apie darbuotojus, kurių gimimo data -
    # 1986-09-19

    def show_employee_by_birthday(self, employee_birthday):
        with self.connect:
            self.cursor.execute(f"""
                SELECT * FROM DARBUOTOJAS
                WHERE ASMENS_KODAS LIKE '%{employee_birthday}%';   
            """)
            return self.cursor.fetchall()

    # 8. Išrinkite darbuotojų vardus, kurių pavardės yra Sabutis

    def select_employee_by_surname(self, employee_surname):
        with self.connect:
            self.cursor.execute(f"""
            SELECT * FROM DARBUOTOJAS
            WHERE PAVARDĖ LIKE '{employee_surname}';
            """)
            return self.cursor.fetchall()

    # 9. Išrinkite duomenis (vardą ir pavardę) apie programuotojus iš Gamybos
    # skyriaus
    def select_employee_by_division(self, employee_division):
        with self.connect:
            self.cursor.execute(f"""
            SELECT VARDAS, PAVARDĖ FROM DARBUOTOJAS
            JOIN SKYRIUS ON SKYRIUS.ID = DARBUOTOJAS.ID
            WHERE PAVADINIMAS LIKE '{employee_division}';        
            """)
        return self.cursor.fetchall()
    # 10. Įterpkite į lentelę “DARBUOTOJAI” naują darbuotoją,
    # užpildydami visus reikiamus laukus (vardą, pavardę, gimimo datą,
    # pareigas ir skyriaus pavadinimą).

    def execute_query(self, query):
        with self.connect:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    # 11. Įterpkite į lentelę “DARBUOTOJAI” naują darbuotoją, užpildydami
    # tik laukus (vardą, pavardę, gimimo datą). Pareigas ir skyriaus
    # pavadinimą palikite neužpildytus.

    def update_employee_data(self, name, surname, identical_id):
        with self.connect:
            self.cursor.execute(f"""
            INSERT INTO DARBUOTOJAS (VARDAS, PAVARDĖ, ASMENS_KODAS)
            VALUES('{name}', '{surname}', {identical_id})
            """)
            return self.cursor.fetchall()

    # 12. Užpildykite likusius tuščius laukus “DARBUOTOJAI” lentelėje,
    # jūsų prieš tai įterptame įraše. Priskirkite darbuotojui pareigas ir skyrių.
    def insert_data(self, duties, start_at, division_id, project_id):
        with self.connect:
            self.cursor.execute(f"""
            UPDATE DARBUOTOJAS SET PAREIGOS='{duties}',
            DIRBA_NUO='{start_at}', SKYRIUS_ID={division_id}, PROJEKTAS_ID={project_id}
            WHERE VARDAS='Wade' AND PAVARDĖ='Wilson';
            """)
            return self.cursor.fetchall()
    # 13. Ištrinkite lentelės “DARBUOTOJAI” įrašą, kurio gimimo
    # data yra tokia, kurią jūs sukūrėte.
    def collect_employee_data(self, employee_birth_date1, employee_birth_date2):
        with self.connect:
            self.cursor.execute(f"""
            SELECT * FROM DARBUOTOJAS
            WHERE ASMENS_KODAS='{employee_birth_date1}'
               OR ASMENS_KODAS='{employee_birth_date2}';
            """)
            return self.cursor.fetchall()
    # 14. Įterpkite, du darbuotojus, pavarde Antanaitis kurių pareigos būtų
    # “Programuotojas”.

    def insert_two_employees(self, employee_surname, duties):
        with self.connect:
            self.cursor.execute(f"""
            INSERT INTO DARBUOTOJAS (PAVARDĖ, PAREIGOS)
            VALUES('{employee_surname}', '{duties}');
            """)
            return self.cursor.fetchall()

    # 15. Pakeiskite, abiejų Antanaičių pareigas į “Testuotojas” vienu sakiniu.
    def change_employee_duties(self, new_employee_duties, employee_surname, current_duties):
        with self.connect:
            self.cursor.execute(f'''
            UPDATE DARBUOTOJAS SET PAREIGOS='{new_employee_duties}'
            WHERE PAVARDĖ='{employee_surname}' AND PAREIGOS='{current_duties}';
            ''')
            return self.cursor.fetchall()

    # 16. Suskaičiuokite, kiek įmonėje dirba Testuotojų.
    def counter_duties(self, name_dutie):
        with self.connect:
            self.cursor.execute(f"""
            SELECT PAREIGOS, COUNT(*) FROM DARBUOTOJAS
            WHERE PAREIGOS LIKE '{name_dutie}'
            GROUP BY PAREIGOS;
            """)
            return self.cursor.fetchall()






