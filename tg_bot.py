import telebot
import NewModule

token = '5122152173:AAGsclruin6d71XL3FWOWdGfguA4aInMKD8'

bot = telebot.TeleBot(token)

games = {}
players = {}


@bot.message_handler(commands=['start'])
def start(message):
    name, surname = message.from_user.first_name, message.from_user.last_name
    ans = f'Hello, {name} {surname}'
    bot.send_message(message.from_user.id, ans)


@bot.message_handler(commands=['create'])
def create(message):
    try:
        game_name = message.text.split()[1]
        players_count = int(message.text.split()[2])
        print(game_name, players_count)
        games[game_name] = NewModule.MyGame(players_count, 7)
        id = message.from_user.id
        players[id] = game_name
        bot.send_message(message.from_user.id, 'Игра успешно создана.')
    except Exception as e:
        print(e)
        bot.send_message(message.from_user.id, 'Вы неправильно указали данные для игры')


@bot.message_handler(commands=['make_step'])
def make_step(message):
    id = message.from_user.id
    message_to_ans = games[players[id]].make_step()
    bot.send_message(message.from_user.id, message_to_ans)


@bot.message_handler(commands=['buy'])
def buy(message):
    id = message.from_user.id
    message_to_ans = games[players[id]].buy(int(message.text.split()[1]))
    message_to_ans += '\n' + games[players[id]].get_data()
    bot.send_message(message.from_user.id, message_to_ans)


bot.polling(none_stop=True, interval=0)
