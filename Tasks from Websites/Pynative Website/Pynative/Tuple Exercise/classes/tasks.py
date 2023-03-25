class ReverseTupleTask1:

    def __init__(self):
        self.tuple = (10, 20, 30, 40, 50)

    def reverse_tuple(self):
        return self.tuple[::-1]


class AccessValueTask2:

    def __init__(self):
        self.tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

    def access_value(self):
        return self.tuple1[1][1]


class CreateTupleTask3:

    def create_tuple(self):
        return (50,)


class UnpackTheTupleTask4:

    def __init__(self):
        self.tuple1 = (10, 20, 30, 40)

    def unpack_tuple(self):
        a, b, c, d = self.tuple1
        print(a)
        print(b)
        print(c)
        print(d)


class SwapTupleTask5:

    def __init__(self):
        self.tuple1 = (11, 22)
        self.tuple2 = (99, 88)

    def swap_tuple(self):
        self.tuple1, self.tuple2 = self.tuple2, self.tuple1
        return self.tuple1, self.tuple2


class CopyFromAnotherTask6:

    def __init__(self):
        self.tuple1 = (11, 22, 33, 44, 55, 66)
        self.tuple2 = ()

    def copy_data(self):
        self.tuple2 = self.tuple1[3:5]
        return self.tuple2


class ModifyTheTupleTask7:

    def __init__(self):
        self.tuple1 = (11, [22, 33], 44, 55)

    def modify_tuple(self):
        self.tuple1[1][0] = 222
        return self.tuple1


class SortTupleTask8:

    def __init__(self):
        self.tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

    def sort_tuple(self):
        return tuple(sorted(list(self.tuple1), key=lambda x: x[1]))


class CountNumberOccurrencesTask9:

    def __init__(self):
        self.tuple1 = (50, 10, 60, 70, 50)

    def count_numbers(self):
        # return sum([1 for number in self.tuple1 if number == 50])
        return self.tuple1.count(50)


class ChefIfValueSameTask10:

    def __init__(self):
        self.tuple1 = (45, 45, 45, 45)

    def check_same_value(self):
        return all(number == self.tuple1[0] for number in self.tuple1)
