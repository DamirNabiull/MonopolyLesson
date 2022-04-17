class MyCell:
    def __init__(self, name, cost, price):
        self.__name = name
        self.__cost = cost
        self.__price = price
        self.__owner = None

    def add_owner(self, owner):
        self.__owner = owner

    def has_owner(self):
        return self.__owner is not None

    def get_owner(self):
        return self.__owner

    def get_name(self):
        return self.__name

    def get_cost(self):
        return self.__cost

    def get_price(self):
        return self.__price

    def get_data(self):
        to_return = ''
        to_return += f'Улица: {self.__name}, Стоимость: {self.__cost}, Цена за попадание: {self.__price}'
        if self.has_owner():
            to_return += f', Владелец: {self.__owner}'
        return to_return

    def print_data(self):
        print(f'Улица: {self.__name}, Стоимость: {self.__cost}, Цена за попадание: {self.__price}', end='')
        if self.has_owner():
            print(f', Владелец: {self.__owner}')
        print()
