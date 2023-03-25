class Coputation:

    def __init__(self):
        pass

    def factorial(self, enter_number: int):
        multiply_factorial = 1
        for factorial in range(1, enter_number + 1):
            multiply_factorial = multiply_factorial * factorial
        return multiply_factorial

    def sum(self, enter_range):
        sum_value = 0
        for number in range(enter_range):
            sum_value += number
        return sum_value

    def test_prime(self, checking_prime):
        is_prime = True
        for i in range(2, checking_prime):
            if checking_prime % i == 0:
                is_prime = False
        if is_prime:
            print(f'Prime number')

    def test_prims(self, start_number, end_number):
        for check_prime in range(start_number, end_number + 1):
            if check_prime > 1:
                for i in range(2, check_prime):
                    if check_prime % i == 0:
                        break
                else:
                    print(check_prime, end=' ')

    def table_multi(self, number_table):
        for i in range(1, 11):
            print(f'{number_table} * {i} = {number_table * i}')

    def all_tables_multi(self):
        for i in range(1, 11):
            for j in range(1, 11):
                print(f'{i} * {j} = {i * j}')

    def list_div(self):
        Ldiv = []
        for i in range(11):
            if i % 2 == 0:
                Ldiv.append(i)
        print(Ldiv)

    def list_div_prim(self, enter_number):
        Ldiv = []
        for i in range(1, enter_number + 1):
            if enter_number % i == 0 and self.test_prime(i):
                Ldiv.append(i)
        print(Ldiv)
