import telebot
import requests
import array
from telebot import types
from telebot.types import Message
TOKEN = '1083085745:AAFrA6XXGKt1KWaWSCh_ylZ6AvFtKCAVNuM'
bot = telebot.TeleBot(TOKEN)








mk = types.ReplyKeyboardMarkup(one_time_keyboard  = True)
btn1 = types.KeyboardButton("Оффициант")
btn2 = types.KeyboardButton("Бот")
mk.add(btn1,btn2)
@bot.edited_message_handler(content_types=['text'])




@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Здравствуйте {0.first_name} !, это ресторан  Qaimaq, ресторан традиционной казахской, уйгурской, узбекской кухни с большой террасой и тенистым садом, арыками и фонтанами.\nСкажите хотите что бы вас обслужил оффициант или бот?".format(message.from_user, bot.get_me()), reply_markup=mk)

menu = types.ReplyKeyboardMarkup(resize_keyboard  = True)
men = types.KeyboardButton("Меню")
menu.add(men)

bluda = types.ReplyKeyboardMarkup(one_time_keyboard  = True, row_width = 1)
gor = types.KeyboardButton("Горячие Закуски")
sal = types.KeyboardButton("Салаты")
sup = types.KeyboardButton("Супы")
napt = types.KeyboardButton("Напитки")
bluda.add(gor,sal,sup,napt)

pic_zelsal = 'https://m.kedem.ru/photo/recipe/rnamebig/salat-na-skoruyu-ruku.jpg'
pic_jark = 'https://pics.botanichka.ru/wp-content/uploads/2018/09/zharenaya-kartoshka-v-duhovke-01.jpg'
pic_kotl= 'https://esh-derevenskoe.ru/image/cache/catalog/recipe/26-550x350.jpg'
pic_ovow = 'https://www.povarenok.ru/data/cache/2019jun/13/01/2550739_89635-710x550x.jpg'
pic_samsa = 'https://alimero.ru/uploads/images/16/38/88/2018/03/21/1d4634_wmark.jpg'
pic_zelsal = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSxuXExdu_y6EjqIFzadE3pmUc6h1rOjarGiaxZU7dX1k2ej6Ah&usqp=CAU'
pic_cezar = 'https://blog-food.ru/images/site/recipes/salads/0009-cezar/12.jpg'
pic_borw = 'https://www.koolinar.ru/all_image/recipes/62/62723/recipe_2151445e-d6f9-4026-a01b-249c8dc4011c_large.jpg'
pic_chk = 'https://ist.say7.info/img0002/31/231_01742a1_2791_6hi.jpg'
pic_turt = 'https://static.1000.menu/img/content/28232/sup-iz-cherepaxi-s-xeresom_1534334357_1_max.jpg'
pic_cola = 'https://pizzamizza.kz/wp-content/uploads/2017/04/cc1.png'
pic_chai = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRZHC0MGFteIn8KFDAhvuEmQVjgdS_w0bkyoHgPuqOUDoFp10jA&usqp=CAU'
pic_compot = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRumD4l-WQh2_C2h9fNyGnk1igk2qVVc4po5zVMFA2KPYCKLXLd&usqp=CAU'

gor1 = types.ReplyKeyboardMarkup(one_time_keyboard= True, row_width = 1)
jark = types.KeyboardButton("Жаренная картошка по по-домашнему (1000тнг)")
samsa = types.KeyboardButton("Самса слоеная 2 шт (800тнг)")
kotl = types.KeyboardButton("Котлеты с пюрешкой(980тнг)")
back1 = types.KeyboardButton("Вернуться обратно в меню")
gor1.add(jark,samsa,kotl,back1)
cnt = 333

bckn = types.ReplyKeyboardMarkup(one_time_keyboard= True, row_width = 1)
yes1 = types.KeyboardButton("Вернуться обратно в меню")
bckn.add(yes1)


sal1 = types.ReplyKeyboardMarkup(one_time_keyboard= True, row_width = 1)
zelsal = types.KeyboardButton("Зеленый листовой салат (1500тнг)")
ovow =  types.KeyboardButton("Овощи по-домашнему (1800тнг)")
cezar = types.KeyboardButton("Цезарь (1500тнг)")
sal1.add(zelsal,ovow,cezar,back1,yes1)

sup1 = types.ReplyKeyboardMarkup(one_time_keyboard= True, row_width = 1)
borw = types.KeyboardButton("Борщ с сметаной(700тнг)")
chk = types.KeyboardButton("Куриный суп(1000тнг)")
turt = types.KeyboardButton("Суп с черепахой(5000тнг)")
sup1.add(borw,chk,turt,yes1)

napt1 = types.ReplyKeyboardMarkup(one_time_keyboard= True, row_width = 1)
cola  =  types.KeyboardButton("Кока-Кола 1литр (340тнг)")
chai  =   types.KeyboardButton("Черный чай (100тнг)")
compt =  types.KeyboardButton("Компот(300тнг)")
napt1.add(cola,chai,compt,yes1)

yn = types.ReplyKeyboardMarkup(one_time_keyboard= True, row_width = 1)
yes = types.KeyboardButton("Подтвердить заказ")
back = types.KeyboardButton("Вернуться обратно в меню")
yn.add(yes,back)

food = ['']
kompot =  'Компот(300тнг)'
ans = types.ReplyKeyboardMarkup(one_time_keyboard= True, row_width = 1)
x1 = types.KeyboardButton("Подтвердить заказ")
x2 = types.KeyboardButton("x2")
x3 = types.KeyboardButton("x3")
sch = types.KeyboardButton("Счет")
ans.add(x1,x2,x3,sch)


@bot.message_handler(func=lambda message: True)
def upper(message: Message):
	if message.chat.type == 'private':
		if message.text == 'Оффициант':
			bot.send_message(message.chat.id, "Хорошо, оффициант подойдет через пару минут. \nУкажите пожалуйста номер своего столика😊(1-5)")
		elif message.text == '1':
			bot.send_message(message.chat.id, 'Хорошо, наш оффициант подойдет к первому столику')
		elif message.text == '2':
			bot.send_message(message.chat.id, 'Хорошо, наш оффициант подойдет к второму столику')
		elif message.text == '3':
			bot.send_message(message.chat.id, 'Хорошо, наш оффициант подойдет к третьему столику')
		elif message.text == '4':
			bot.send_message(message.chat.id, 'Хорошо, наш оффициант подойдет к четвертому столику')
		elif message.text == '5':
			bot.send_message(message.chat.id, 'Хорошо, наш оффициант подойдет к пятому столику')
		elif message.text == 'Бот':
			bot.send_message(message.chat.id, "Хорошо, наш бот всегда готов к вашим услугам 😊", reply_markup = menu) 
		elif message.text == 'Меню':
			bot.send_message(message.chat.id, "Выберите блюда", reply_markup = bluda)
		elif message.text == 'Горячие Закуски':
			bot.send_message(message.chat.id, "Нажмите на блюдо что бы узнать про него", reply_markup = gor1)
		elif message.text == 'Жаренная картошка по по-домашнему (1000тнг)':
			bot.send_photo(message.chat.id, pic_jark) and bot.send_message(message.chat.id, "Ингриденты:   3 картошки прожаренным в масле ", reply_markup = yn)
		elif message.text == 'Самса слоеная 2 шт (800тнг)':
			bot.send_photo(message.chat.id, pic_samsa) and bot.send_message(message.chat.id, "Ингриденты:  Мясо,тесто,лук", reply_markup = yn)
		elif message.text == 'Котлеты с пюрешкой(980тнг)':
			bot.send_photo(message.chat.id, pic_kotl) and bot.send_message(message.chat.id, "Ингриденты:  Картошка,мясо,лук", reply_markup = yn)
		elif message.text == 'Салаты':
			bot.send_message(message.chat.id, "Нажмите на блюдо что бы узнать про него", reply_markup = sal1)
		elif message.text == 'Зеленый листовой салат (1500тнг)':
			bot.send_photo(message.chat.id, pic_zelsal) and bot.send_message(message.chat.id, "Ингриденты:\n 2 капусты\n 3 картошки \n ", reply_markup = yn)
		elif message.text == 'Овощи по-домашнему (1800тнг)':
			bot.send_photo(message.chat.id, pic_ovow) and bot.send_message(message.chat.id, "Ингриденты: 3 оругца и 3 помидора смешанный с майонезом ", reply_markup = yn)	
		elif message.text == 'Цезарь (1500тнг)':
			bot.send_photo(message.chat.id, pic_cezar) and bot.send_message(message.chat.id, "Ингриденты: курица, салат и сыр ", reply_markup = yn)
		elif message.text == 'Горячие Закуски':
			bot.send_message(message.chat.id, "Нажмите на блюдо что бы узнать про него", reply_markup = gor1)
		elif message.text == 'Супы':
			bot.send_message(message.chat.id, "Нажмите на блюдо что бы узнать про него", reply_markup = sup1)	
		elif message.text == 'Борщ с сметаной(700тнг)':
			bot.send_photo(message.chat.id, pic_borw) and bot.send_message(message.chat.id, "Ингриденты: вода,мясо,капуста ", reply_markup = yn)
		elif message.text == 'Куриный суп(1000тнг)':
			bot.send_photo(message.chat.id, pic_chk) and bot.send_message(message.chat.id, "Ингриденты: курица, вода и соль ", reply_markup = yn)
		elif message.text == 'Суп с черепахой(5000тнг)':
			bot.send_photo(message.chat.id, pic_turt) and bot.send_message(message.chat.id, "Ингриденты: черепаха и вода ", reply_markup = yn)
		elif message.text == 'Напитки':
			bot.send_message(message.chat.id, "Нажмите на блюдо что бы узнать про него", reply_markup = napt1)	
		elif message.text == 'Кока-Кола 1литр (340тнг)':
			bot.send_photo(message.chat.id, pic_cola , reply_markup = yn) 
		elif message.text == 'Черный чай (100тнг)':
			bot.send_photo(message.chat.id, pic_chai) and bot.send_message(message.chat.id, "Ингриденты: вода ", reply_markup = yn)
		elif message.text == 'Компот(300тнг)':
			bot.send_photo(message.chat.id, pic_compot) and bot.send_message(message.chat.id, "Ингриденты вода и  ", reply_markup = yn)
		elif message.text == 'Подтвердить заказ':
			bot.send_message(message.chat.id, "Данное блюдо добавлен в корзину, cколько порции вам?", reply_markup = ans)
		elif message.text == 'Добавить в корзину Куриный суп(1000тнг)':
			bot.send_message(message.chat.id, "Данное блюдо добавлен в корзину, cколько порции вам?", reply_markup = ans)
		elif message.text == 'Добавить в корзину':
			bot.send_message(message.chat.id, "Данное блюдо добавлен в корзину, cколько порции вам?", reply_markup = ans)
		elif message.text == 'x1':
			bot.send_message(message.chat.id, "Хорошо", reply_markup = bluda) 
		elif message.text == 'x2':
			bot.send_message(message.chat.id,"Хорошо", reply_markup = bluda)
		elif message.text == 'x3':
			bot.send_message(message.chat.id, "Хорошо", reply_markup = bluda)
		elif message.text == 'Вернуться обратно к салатам': 
			bot.send_message(message.chat.id, "Нажмите на блюдо что бы узнать про него", reply_markup = sal1)
		elif message.text == 'Счет':
			bot.send_message(message.chat.id, f'Счет: {food}')
		elif message.text == 'Вернуться обратно в меню':
			bot.send_message(message.chat.id, "Выберите блюда", reply_markup = bluda)
		else:
			bot.send_message(message.chat.id, "Извините кажется вы ошиблись =(") and bot.send_message(message.chat.id, f'Счет: {cnt}')




bot.polling()