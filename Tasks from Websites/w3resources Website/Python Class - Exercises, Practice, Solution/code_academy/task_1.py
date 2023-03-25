from itertools import count

from clases.task_1 import Sentence

Sentence(enter_txt='Entering').make_text_backwards()
Sentence(enter_txt='HELLOWORLD').return_text_lower()
Sentence(enter_txt='hello world').return_text_upper()
Sentence(enter_txt='What I am doing now').return_how_many_words()
Sentence(enter_txt='Hello, world.!').return_how_many_symbols()
Sentence(enter_txt='Hello I have 19 years old').return_how_many_digits()


count_lower_case = Sentence(enter_txt='HELLOWORLD').return_text_lower()
count_upper_case = Sentence(enter_txt='hello world').return_text_upper()
count_words = Sentence(enter_txt='What I am doing now').return_how_many_words()
count_digits = Sentence(enter_txt='Hello I have 19 years old').return_how_many_digits()

count_object = print(f'''Lower case: {count_lower_case},
Upper case: {count_upper_case},
Count words: {count_words}, 
Count digits {count_digits}''')
