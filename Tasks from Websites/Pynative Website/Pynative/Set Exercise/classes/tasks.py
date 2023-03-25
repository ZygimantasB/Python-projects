class AddElementToSetTask1:

    def __init__(self):
        self.sample_set = {"Yellow", "Orange", "Black"}
        self.sample_list = ["Blue", "Green", "Red"]

    def list_set(self):
        self.sample_set.update(self.sample_list)
        return set(self.sample_set)


class IdenticalValuesTask2:

    def __init__(self):
        self.set1 = {10, 20, 30, 40, 50}
        self.set2 = {30, 40, 50, 60, 70}

    def same_value(self):
        return set.intersection(self.set1, self.set2)


class OnlyUniqueTask3:

    def __init__(self):
        self.set1 = {10, 20, 30, 40, 50}
        self.set2 = {30, 40, 50, 60, 70}

    def unique_value(self):
        return set.union(self.set1, self.set2)


class RemoveItemsTask4:

    def __init__(self):
        self.set1 = {10, 20, 30, 40, 50}
        self.set2 = [10, 20, 30]

    def remove_items(self):
        self.set1.difference_update(self.set2)
        return self.set1
        # set_dict = {}
        # for i in self.set1:
        #     if i == 10 or i == 20 or i == 30:
        #         continue
        #     else:
        #         print(i)


class ReturnSetElementsTask5:

    def __init__(self):
        self.set1 = {10, 20, 30, 40, 50}
        self.set2 = {30, 40, 50, 60, 70}

    def return_elements(self):
        return self.set1.symmetric_difference(self.set2)


class CheckTwoSetsTask7:

    def __init__(self):
        self.set1 = {10, 20, 30, 40, 50}
        self.set2 = {60, 70, 80, 90, 10}

    def check_sets(self):
        return set.intersection(self.set1, self.set2)


class UpdateListsTask8:

    def __init__(self):
        self.set1 = {10, 20, 30, 40, 50}
        self.set2 = {30, 40, 50, 60, 70}

    def update_lists(self):
        return sorted(set.symmetric_difference(self.set1, self.set2))


class RemoveCommonItemsTask9:

    def __init__(self):
        self.set1 = {10, 20, 30, 40, 50}
        self.set2 = {30, 40, 50, 60, 70}

    def remove_common(self):
        self.set1.intersection_update(self.set2)
        return self.set1

