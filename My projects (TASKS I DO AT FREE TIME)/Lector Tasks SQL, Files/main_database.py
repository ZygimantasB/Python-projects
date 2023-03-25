from classes.working_db import DatabaseInformation

# database = DatabaseInformation('amazing.db')
#
# database.create_table()
# database.insert_into_table()
# print(database.execute_query('SELECT * FROM Super_table'))

database_file = DatabaseInformation(database_name='count_words_final.db',
                                    table_name='symbols_counting_NY',
                                    file_name='new_york.txt',
                                    first_colum_name='NY_Symbols',
                                    second_column_name='NY_Counting',
                                    what_to_count='symbols')
# database_file.execute_query('DROP TABLE words_counting')
# database_file.create_table()
# database_file.count_words_symbols()

# print(database_file.execute_query('SELECT * FROM symbols_counting_NY'))
# print(database_file.execute_query('SELECT * FROM symbols_counting_London'))
# print(database_file.execute_query('SELECT * FROM words_counting_London JOIN words_counting_NY ON '
#                                   'ID_LONDON_WORDS = ID_NEW_YORK_WORDS'))
# print(database_file.execute_query('SELECT London_Words, SUM(London_Counting + NY_Counting) FROM '
#                                   'words_counting_London JOIN words_counting_NY ON '
#                                   'ID_NEW_YORK_WORDS = ID_LONDON_WORDS GROUP BY London_Words'))
# print(database_file.execute_query('SELECT NY_Words, SUM((London_Counting + NY_Counting) - '
#                                   'words_counting_NY.NY_Counting) FROM words_counting_London LEFT '
#                                   'JOIN words_counting_NY ON ID_LONDON_WORDS = ID_NEW_YORK_WORDS '
#                                   'GROUP BY London_Words'))

print(database_file.execute_query("SELECT NY_Words, NY_Counting FROM words_counting_London JOIN "
                                  "words_counting_NY ON ID_LONDON_WORDS = ID_NEW_YORK_WORDS WHERE NY_Words LIKE "
                                  "'%London%'"))

print(database_file.execute_query("SELECT London_Words, London_Counting FROM "
                                  "words_counting_London join words_counting_NY ON "
                                  "ID_LONDON_WORDS = ID_NEW_YORK_WORDS WHERE London_Words LIKE '%York%'"))

print(database_file.execute_query("SELECT * FROM words_counting_NY JOIN words_counting_London ON "
                                  "ID_NEW_YORK_WORDS = ID_LONDON_WORDS WHERE NY_Words LIKE '%' || words_counting_London.London_Words || '%'"))

