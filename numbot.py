import telebot
import config 
from random import randint


number = (randint(0, 9))
running = True


bot = telebot.TeleBot(config.token)

@bot.randomnums(commands=['start']
def start_message(message):
	guess = int(input('Введите целое число: '))
	if guess == number:
		print("Я хочу сказать, шо ты выиграл)")
		running = False
	elif guess < number:
		print("Ну, не повезло, немного больше")
		running = True
	else:
		print("Меньше")
		running = True
	print("ЗАВЕРШЕНО, ПРАВИЛЬНЫЙ ОТВЕТ БЫЛ - " + str(number))

		



#я надеюсь, ты без коментариев понимаешь, что это тупа угадайка, от 0 до 9)))




heroku login blackpoetnik@gmail.com Slognone1337.
heroku create --region eu numbotrandom #Не забываемпоменять имя приложения
#P.S. в имени могут быть только буквы в нижнем регитсре, цифры  и тире.
heroku addons:create heroku-redis:hobby-dev -a numbotrandom #И снова меняем имя!
heroku buildpacks:set heroku/python
git push heroku master
heroku ps:scale bot=1 # запускаем бота
heroku logs --tail #включаем логи