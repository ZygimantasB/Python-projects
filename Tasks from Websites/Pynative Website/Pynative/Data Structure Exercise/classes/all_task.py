import itertools


class DataStructureTask1:
    def task_1(self, list_first_odd, list_second_even):
        odd_list = []
        even_list = []

        odd_list.append([odd_number for odd_number in list_first_odd if
                         odd_number % 2 != 0])
        even_list.append([even_number for even_number in list_second_even if
                          even_number % 2 == 0])

        # result = [j for i in [odd_list, even_list] for j in i]
        # print(result)

        # odd_list.extend(even_list)
        # print(odd_list)

        # result = [*odd_list, *even_list]

        result = list(itertools.chain(odd_list, even_list))

        print(result)


class DataStructureTask2:
    def task_2(self, numbers_list):
        index_4 = numbers_list.pop(4)
        print('List After removing element at index 4', numbers_list)
        numbers_list.insert(2, index_4)
        print('List after Adding element at index 2', numbers_list)
        numbers_list.append(index_4)
        print('List after Adding element at last', numbers_list)


class DataStructureTask3:
    def slice_list_in_reverse(self, numbers_list):
        length = len(numbers_list)
        chunk_size = int(length / 3)
        start = 0
        end = chunk_size
        for i in range(3):
            indexes = slice(start, end)
            list_chunk = numbers_list[indexes]
            print(list_chunk)
            start = end
            end += chunk_size


class DataStructureTask4:
    def __init__(self, new_list):
        self.new_list = new_list

    def count_numbers(self):
        count = {}
        unique_numbers = self.new_list
        for i in self.new_list:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        print(count)


class DataStructureTask5:
    def __init__(self, first_list, second_list):
        self.fist_list = first_list
        self.second_list = second_list

    def set_in_pair(self):
        # for first, second in zip(self.fist_list, self. second_list):
        #     result = first, second
        #     print(f'Result is {result}, ', end='')
        result = set(zip(self.fist_list, self.second_list))
        print('Result is:', result)


class DataStructureTask6:
    def __init__(self, first_numbers, second_numbers):
        self.first_numbers = first_numbers
        self.second_numbers = second_numbers

    def unique_numbers_from_sets(self):
        unique_numbers = set.intersection(self.first_numbers,
                                          self.second_numbers)
        for item in unique_numbers:
            self.first_numbers.remove(item)
        print(self.first_numbers)


class DataStructureTask7:
    def __init__(self, first_set, second_set):
        self.first_set = first_set
        self.second_set = second_set

    def set_superset_issubset(self):
        first_subset_second = self.first_set.issubset(self.second_set)
        print('First set is subset of second set:', first_subset_second)
        second_subset_first = self.second_set.issubset(self.first_set)
        print('First set is subset of second set:', second_subset_first)
        first_superset_second = self.first_set.issuperset(self.second_set)
        print('First set is Super set of second set: ', first_superset_second)
        second_superset_first = self.second_set.issuperset(self.first_set)
        print('Second set is Super set of First set', second_superset_first)

        if self.first_set.issubset(self.second_set):
            self.first_set.clear()
        print(self.first_set)
        if self.second_set.issubset(self.first_set):
            self.second_set.clear()
        print(self.second_set)


class DataStructureTask8:

    def __init__(self, list_checking, dict_checking):
        self.list_check = list_checking
        self.dict_check = dict_checking

    def removing_data(self):
        # for item in self.list_check:
        #     if item in self.dict_check.values():
        #         print(item, sep=' ')
        result = [number for number in self.list_check if number in
                  self.dict_check.values()]
        return result


class DataStructureTask9:

    def __init__(self, remove_duplicate):
        self.remove = remove_duplicate
        self.unique_number_list = []

    def fixing_dict(self):
        print(self.remove)
        for number in self.remove.values():
            if number not in self.unique_number_list:
                self.unique_number_list.append(number)
        return 'unique number', self.unique_number_list

                #     self.unique_number_list.append(number)
        # return set(self.unique_number_list)


class DataStructureTask10:

    def __init__(self, numbers_list):
        self.numbers_list = numbers_list

    def remove_duplicate_return_max_min(self):
        new_list = [*set(self.numbers_list)]
        print('unique items', new_list)
        print('tuple', tuple(new_list))
        min_number = self.numbers_list[0]
        max_number = self.numbers_list[0]
        for number in self.numbers_list:
            if number > max_number:
                max_number = number
            elif number < min_number:
                min_number = number
        print('min:', max_number)
        print('max:', min_number)