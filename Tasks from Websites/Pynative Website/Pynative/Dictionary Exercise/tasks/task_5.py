from random import sample

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

new_value = {key: sample_dict[key] for key in keys}

print(new_value)
