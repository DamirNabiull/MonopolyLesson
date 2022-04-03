class MyPlayer:
    def __init__(self, money):
        self.__position = 0
        self.__money = money

    def spend_money(self, cost):
        self.__money -= cost

    def set_position(self, step, map_size):
        self.__position = (self.__position + step) % map_size

    def get_position(self):
        return self.__position

    def print_data(self):
        print(f'Позиция: {self.__position}, Деньги: {self.__money}')
