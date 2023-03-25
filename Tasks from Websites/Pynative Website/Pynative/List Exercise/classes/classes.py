class ReverseListTask1:

    def __init__(self, numbers_list):
        self.numbers_list = numbers_list

    def revers_list(self):
        # return self.numbers_list[::-1]
        return list(reversed(self.numbers_list))


class ConcatTwoListsTask2:

    def __init__(self, string_list1, string_list2):
        self.string_list1 = string_list1
        self.string_list2 = string_list2

    def concat_list(self):
        # return list(zip(self.string_list1, self.string_list2))

        # self.string_list1.append(self.string_list2)
        # return self.string_list1

        # [self.string_list1.append(item) for item in
        #  self.string_list2]
        # return self.string_list1

        # return self.string_list1 + self.string_list2

        # self.string_list1.extend(self.string_list2)
        # return self.string_list1

        return [self.string_list1 + self.string_list2 for
                self.string_list1, self.string_list2 in zip(
                 self.string_list1, self.string_list2)]


class SquareListTask3:

    def __init__(self):
        self.number_list: list = [1, 2, 3, 4, 5, 6, 7]
        self.square_list_print: list = []

    def square_list(self):
        self.square_list_print.append([number**2 for number in
                                      self.number_list])
        return self.square_list_print


class ConcatTwoListTask4:

    def __init__(self):
        self.list1 = ["Hello ", "take "]
        self.list2 = ["Dear", "Sir"]
        self.append_list = []

    def concat_list(self):
        self.append_list.append([number1 + number2 for number1 in self.list1
                                 for
                                 number2 in \
                                 self.list2])
        return self.append_list

        # for number1 in self.list1:
        #     for number2 in self.list2:
        #         result = number1 + number2
        #         self.append_list.append(result)
        # return self.append_list


class IterateListTask5:

    def __init__(self):
        self.list1 = [10, 20, 30, 40]
        self.list2 = [100, 200, 300, 400]

    def iterate_list(self):
        # return [[number1, number2] for number1, number2 in zip(self.list1,
        #                                                 self.list2)]

        # for number1, number2 in zip(self.list1, self.list2[::-1]):
        #     print(number1, number2)

        # return map(list, zip(self.list1, self.list2))

        # return [[self.list1[number], self.list2[number]] for number in range(
        #     min(len(self.list1), len(self.list2)))]

        result = {key: value for key, value in zip(self.list1, self.list2)}
        return result


class RemoveEmptyStringTask6:
    def __init__(self):
        self.list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

    def remove_empty(self):
        return list(filter(None, self.list1))


class AddNewItemTask7:

    def __init__(self):
        self.list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

    def append_item(self):
        self.list1[2][2].append(7000)
        return self.list1


class ExtendNestedListTask8:

    def __init__(self):
        self.list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
        self.sub_list = []

    def append_item(self):
        self.list1[2][1][2].extend(self.sub_list)
        return self.list1


class ReplaceItemTask9:
    def __init__(self):
        self.list1 = [5, 10, 15, 20, 25, 50, 20]

    def replace_item(self, number_change):
        new_value = self.list1.index(20)
        self.list1[new_value] = 200
        return self.list1


class RemoveSpecificItemTask10:
    def __init__(self):
        self.list1 = [5, 20, 15, 20, 25, 50, 20]

    def remove_specific_item(self, number_remove):
        return [number for number in self.list1 if number != number_remove]
    