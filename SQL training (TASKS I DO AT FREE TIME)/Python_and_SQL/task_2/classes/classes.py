import sqlite3


class LecturesDB:
    def __init__(self):
        self.connect = sqlite3.connect('lectures_data.db')
        self.cursor = self.connect.cursor()

    def create_table(self, name_table):
        with self.connect:
            self.cursor.execute(f"""
            CREATE TABLE {name_table} (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            lecture_name VARCHAR(50) NOT NULL,
            teacher VARCHAR(50) NOT NULL,
            duration INT NOT NULL);
            """)
            self.cursor.fetchall()

    def insert_into_table(self, lecture_name, teacher, duration):
        with self.connect:
            self.cursor.execute(f"""
            INSERT INTO lecture_information(lecture_name, teacher, duration)
            VALUES ('{lecture_name}', '{teacher}', {duration});
            """)
            return self.cursor.fetchall()

    def execute_query(self, query):
        with self.connect:
            self.cursor.execute(query)
            return self.cursor.fetchall()

    def renew_lecture_name(self, new_lecture_name):
        with self.connect:
            self.cursor.execute(f"""
            UPDATE lecture_information SET lecture_name  = '{new_lecture_name}'
            WHERE teacher = 'Donatas' AND duration = 80;
            """)
            return self.cursor.fetchall()

    def delete_lecture_by_lector_name(self, lector_name):
        with self.connect:
            self.cursor.execute(f"""
            DELETE FROM lecture_information
            WHERE teacher = '{lector_name}';
            """)
            return self.cursor.fetchall()
