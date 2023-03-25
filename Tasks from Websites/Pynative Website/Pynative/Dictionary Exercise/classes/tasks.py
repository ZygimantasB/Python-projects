import pprint

class ConvertTwoListsTask1:

    def __init__(self):
        self.keys = ['Ten', 'Twenty', 'Thirty']
        self.values = [10, 20, 30]

    def combine_lists(self):
        combined_dict = {}
        # return {key: value for key, value in zip(self.keys, self.values)}
        # return map(list(zip(self.keys, self.values)))
        # return dict(zip(self.keys, self.values))
        for item in range(len(self.keys)):
            combined_dict.update({self.keys[item]: self.values[item]})
        return combined_dict


class MergeDictTask2:

    def __init__(self):
        self.dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
        self.dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

    def merged_dict(self):
        # self.dict1.update(self.dict2)
        # return self.dict1
        return {**self.dict1, **self.dict2}


class FindNumberTask3:
    def __init__(self):
        self.sampleDict = {
            "class": {
                "student": {
                    "name": "Mike",
                    "marks": {
                        "physics": 70,
                        "history": 80
                    }
                }
            }
        }

    def return_number(self):
        return self.sampleDict['class']['student']['marks']['history']


class InitializeDictionaryTask4:

    def __init__(self):
        self.employees = ['Kelly', 'Emma']
        self.defaults = {"designation": 'Developer', "salary": 8000}

    def initialize_dictionary(self):
        return dict.fromkeys(self.employees, self.defaults)


class CreateDictionaryTask5:

    def __init__(self):
        self.sample_dict = {
            "name": "Kelly",
            "age": 25,
            "salary": 8000,
            "city": "New york"}
        self.keys = ["name", "salary"]

    def create_dictionary(self):
        names_dict = {}
        # return {key: self.sample_dict[key] for key in self.keys}

        for key in self.keys:
            names_dict.update({key: self.sample_dict[key]})
        return names_dict


class DeleteListTask6:

    def __init__(self):
        self.sample_dict = {
            "name": "Kelly",
            "age": 25,
            "salary": 8000,
            "city": "New york"}
        self.keys = ["name", "salary"]

    def delete_items(self):
        # return {key: self.sample_dict[key] for key in self.sample_dict if
        #          key not in self.keys}

        # return {key: self.sample_dict[key] for key in self.sample_dict.keys() -
        #         self.keys}

        self.sample_dict.pop(*list([key for key in self.keys]))
        return self.sample_dict


class CheckIfExistsTask7:

    def __init__(self):
        self.sample_dict = {'a': 100, 'b': 200, 'c': 300}
        self.check_value = '200'

    def check_if_exists(self):
        if 200 in self.sample_dict.values():
            result = f'{self.check_value} present in a dict'
        else:
            result = 'Not in'
        return result


class RenameKeyTask8:

    def __init__(self):
        self.sample_dict = {
            "name": "Kelly",
            "age":25,
            "salary": 8000,
            "city": "New york"
        }

    def rename_key(self):
        self.sample_dict['location'] = self.sample_dict.pop('city')
        return self.sample_dict


class GetMinimumValueTask9:

    def __init__(self):
        self.sample_dict = {
            'Physics': 82,
            'Math': 65,
            'history': 75
        }

    def minimum_value(self):
        return min([value for value in self.sample_dict])

        # return min(self.sample_dict, key=self.sample_dict.get)


class ChangeValueTask10:

    def __init__(self):
        self.sample_dict = {
            'emp1': {'name': 'Jhon', 'salary': 7500},
            'emp2': {'name': 'Emma', 'salary': 8000},
            'emp3': {'name': 'Brad', 'salary': 500}
        }

    def change_value(self):
        self.sample_dict['emp2']['salary'] = 8500
        return pprint.pprint(self.sample_dict)
