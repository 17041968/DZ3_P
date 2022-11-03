#Создайте скрипт бота, который находит ответы на фразы по ключу в словаре

dictionary = \
	{
		'Привет': 'Приветик',
		'Как тебя зовут?': 'Меня зовут Анатолий',
		'Выход': 'До свидания!'
	}

isStarted = True
while isStarted:
	var = input("Я: ")
	if var == 'Выход':
		isStarted = not isStarted
	if var in dictionary.keys():
		print('Бот:', dictionary[var])
	else:
		print('Бот:', 'неизвестная команда')