from math import ceil


class Number:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return self.number == other

    def __gt__(self, other):
        return self.number > other

    def __ceil__(self):
        self.number = ceil(self.number)
        print('Округляем...')
        return self.number

    def __add__(self, other):
        return self.number + other

    def __sub__(self, other):
        return self.number - other

    def __floordiv__(self, other):
        return self.number // other

    def __iadd__(self, other):
        self.number += other
        return self.number

    def __str__(self):
        return f'сейчас number = {self.number}'


if __name__ == '__main__':
    number = Number(10.3)
    print(number)
    print(number > 3)
    print(ceil(number))
    print(number + 3)
    print(number)
    number += 20
