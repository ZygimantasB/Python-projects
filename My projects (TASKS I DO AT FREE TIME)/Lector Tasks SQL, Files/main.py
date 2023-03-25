from classes.work_files import CityInformation

city_information = CityInformation('London.txt')

print(city_information.read_information())
print(city_information.count_words())
print(city_information.count_symbols())
print(city_information.words_with_symbol(characters="abcdefgh"))
