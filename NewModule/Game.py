from NewModule.Map import MyMap
from NewModule.Player import MyPlayer
import random


class MyGame:
    def __init__(self, players, streets):
        self.__turn = 0
        self.players = []
        self.game_map = MyMap(streets)
        for i in range(players):
            self.players.append(MyPlayer(1000))

    def start_game(self):
        while 1:
            for i in range(len(self.players)):
                print(f'Ход игрока под номером {i+1}. Нажмите ENTER чтоб бросить кубик!')
                input()
                self.__turn = i
                step = random.randint(1, 7)
                print(f'На кубике выпало число {step}')
                self.players[i].set_position(step, self.game_map.get_size())
                ind = self.players[i].get_position()
                print(f'Вы находитесь на клетке {ind}')
                self.game_map.map[ind].print_data()
                self.offer_to_buy(ind)
                print(f'Ход игрока под номером {i+1} закончен.')
                self.players[i].print_data()
                print('Ход переходит другому игроку \n\n\n')

    def offer_to_buy(self, ind):
        if not self.game_map.map[ind].has_owner():
            print(f'Хотите ли вы приобрести клетку \"{self.game_map.map[ind].get_name()}\"?')
            print(f'[1] - Купить, [2] - Отказаться')
            self.__want_to_buy(ind)
        elif self.game_map.map[ind].get_owner() - 1 != self.__turn:
            print(f'Вы платите за посещение клетки {self.game_map.map[ind].get_price()} рублей!')
            self.players[self.__turn].spend_money(self.game_map.map[ind].get_price())

    def __want_to_buy(self, ind):
        answer = None
        while answer is None:
            try:
                answer = int(input())
                if 0 < answer < 3:
                    break
                answer = None
                print('Введите число(1 или 2)!')
            except Exception as e:
                print('Введите число(1 или 2)!')

        if answer == 1:
            self.game_map.map[ind].add_owner(self.__turn+1)
            self.players[self.__turn].spend_money(self.game_map.map[ind].get_cost())
            print(f'Покупка совершена успешно')
        else:
            print(f'Вы отказались от покупки')
