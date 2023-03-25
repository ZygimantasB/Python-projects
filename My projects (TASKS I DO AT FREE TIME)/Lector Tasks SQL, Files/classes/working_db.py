import sqlite3
from classes.work_files import CityInformation


class DatabaseInformation(CityInformation):

    def __init__(self, database_name: str, file_name: str, table_name: str, first_colum_name: str,
                 second_column_name: str, what_to_count: str):
        super().__init__(file_name)
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self.table_name: str = table_name
        self.first_colum_name: str = first_colum_name
        self.second_column_name: str = second_column_name
        self.what_to_count = what_to_count.casefold()

    def execute_query1(self, query) -> str:
        """
        Run my SQL query
        """
        connection = False
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as error:
            return "Query failed: " + str(error)
        finally:
            if connection:
                connection.close()
        return "Query executed"

    def create_table(self) -> None:
        """
        Create table
        """
        with self.connection:
            self.cursor.execute(f"""
            CREATE TABLE {self.table_name}
            (ID_{(self.file_name.split('.')[0].upper())}_{self.what_to_count.upper()} INTEGER 
            PRIMARY KEY 
            AUTOINCREMENT,
            {self.first_colum_name} TEXT,
            {self.second_column_name} INTEGER)
            """)
            self.cursor.fetchall()

    def insert_into_table(self, table_1st_column_str: str, table_2sec_column_int: str) -> None:
        """
        Insert information into table
        """
        with self.connection:
            self.cursor.execute(f"""
        INSERT INTO {self.table_name} ({self.first_colum_name}, {self.second_column_name})
        VALUES (?, ?)
        """, (table_1st_column_str, table_2sec_column_int))
            self.connection.commit()

    def execute_query(self, query) -> list:
        """
        Run SQL query
        """
        with self.connection:
            self.cursor.execute(query)
            return self.cursor.fetchall()

    def count_words_symbols(self) -> None:
        """
        Counting words and symbols
        """
        if self.what_to_count == 'words':
            counted_words = self.count_words()
            for counting in counted_words:
                self.insert_into_table(table_1st_column_str=counting[0],
                                       table_2sec_column_int=counting[1])
        elif self.what_to_count == 'symbols':
            counting_symbols = self.count_symbols()
            for counting in counting_symbols:
                self.insert_into_table(table_1st_column_str=counting[0],
                                       table_2sec_column_int=counting[1])
