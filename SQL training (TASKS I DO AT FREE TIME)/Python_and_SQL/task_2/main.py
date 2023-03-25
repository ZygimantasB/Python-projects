from classes.classes import LecturesDB

lecture_db = LecturesDB()

# lecture_db.create_table('lecture_information')
# lecture_db.insert_into_table(lecture_name='Vadyba', teacher='Domantas', duration=40)
# lecture_db.insert_into_table(lecture_name='Python', teacher='Donatas', duration=80)
# lecture_db.insert_into_table(lecture_name='Java', teacher='Tomas', duration=80)
# print(lecture_db.execute_query("""
# SELECT * FROM lecture_information
# WHERE duration > 50;
# """))

# lecture_db.renew_lecture_name(new_lecture_name='Python programing')

# lecture_db.delete_lecture_by_lector_name(lector_name='Tomas')

print(lecture_db.execute_query('SELECT * FROM lecture_information'))

