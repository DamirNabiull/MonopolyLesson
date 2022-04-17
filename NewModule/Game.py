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

    def make_step(self):
        i = 0
        self.__turn = i
        step = random.randint(1, 7)
        message_to_return = f'На кубике выпало число {step}\n'
        self.players[i].set_position(step, self.game_map.get_size())
        ind = self.players[i].get_position()
        message_to_return += f'Вы находитесь на клетке {ind}\n'
        message_to_return += self.game_map.map[ind].get_data()
        if not self.game_map.map[ind].has_owner():
            message_to_return += f'\nХотите ли вы приобрести клетку \"{self.game_map.map[ind].get_name()}\"?\n'
            message_to_return += f'/buy 1 - Купить, /buy 2 - Отказаться\n'
        elif self.game_map.map[ind].get_owner() - 1 != self.__turn:
            message_to_return += f'\nВы платите за посещение клетки {self.game_map.map[ind].get_price()} рублей!\n'
            self.players[self.__turn].spend_money(self.game_map.map[ind].get_price())
            owner = self.game_map.map[ind].get_owner()
            self.players[owner-1].add_money(self.game_map.map[ind].get_price())
        return message_to_return

    def buy(self, answer):
        ind = self.players[0].get_position()
        if self.game_map.map[ind].has_owner():
            return 'Не возможно купить. Делайте ход.'
        if answer == 1:
            self.game_map.map[ind].add_owner(self.__turn+1)
            self.players[self.__turn].spend_money(self.game_map.map[ind].get_cost())
            return 'Покупка совершена успешно'
        else:
            return 'Вы отказались от покупки'

    def get_data(self):
        self.bot_steps()
        return self.players[0].get_data()

    def bot_steps(self):
        for i in range(1, len(self.players)):
            print(f'Ход игрока под номером {i + 1}. Нажмите ENTER чтоб бросить кубик!')
            # input()
            self.__turn = i
            step = random.randint(1, 7)
            print(f'На кубике выпало число {step}')
            self.players[i].set_position(step, self.game_map.get_size())
            ind = self.players[i].get_position()
            print(f'Вы находитесь на клетке {ind}')
            self.game_map.map[ind].print_data()
            self.offer_to_buy(ind)
            print(f'Ход игрока под номером {i + 1} закончен.')

            if self.check_lose():
                print(f'Игра закончена, проиграл игрок {i + 1}.\n\n\n')
                break

            self.players[i].print_data()
            print('Ход переходит другому игроку \n\n\n')

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

                if self.check_lose():
                    print(f'Игра закончена, проиграл игрок {i+1}.\n\n\n')
                    break

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
            owner = self.game_map.map[ind].get_owner()
            self.players[owner-1].add_money(self.game_map.map[ind].get_price())

    def __want_to_buy(self, ind):
        answer = random.randint(1, 3)

        if answer == 1:
            self.game_map.map[ind].add_owner(self.__turn+1)
            self.players[self.__turn].spend_money(self.game_map.map[ind].get_cost())
            print(f'Покупка совершена успешно')
        else:
            print(f'Вы отказались от покупки')

    def check_lose(self):
        for player in self.players:
            if player.is_lose():
                return True
        return False
