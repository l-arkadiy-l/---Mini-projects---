# Реализуйте класс Car и унаследуйте от него несколько машин
# Реализуйте класс Human, который будет принимать имя покупателя,
# сколько у него денег.
# Сделайте так, чтобы покупатель мог покупать машины.
class Human:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def buy_car(self, car):
        if self.budget - car.money >= 0:
            print(f'Машина марки {car.brand} куплена за {car.money}')
            self.budget -= car.money
            print(f'У вас осталось {self.budget} рублей')
        else:
            print(f'{self.name}.У вас недостаточно денег для покупки этой машины')


class Car:
    def __init__(self, brand, speed, money):
        if speed > 200:
            money *= 1.5
        self.brand = brand
        self.money = money


class BMW(Car):
    def __init__(self, speed, money):
        super(BMW, self).__init__('BWM', speed, money)


class Lada(Car):
    def __init__(self, speed, money):
        super(Lada, self).__init__('Lada', speed, money)

# examples
if __name__ == '__main__':
    bmv_x6 = BMW(240, 5840000)
    lada_vaz = Lada(130, 300000)
    human = Human('Vladimir', 5400000)
    human.buy_car(lada_vaz)
    human.buy_car(lada_vaz)
