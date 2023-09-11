#Game
from random import *
win=randint(1, 10)
print(f'Привет! Попробуй угадать через сколько чисел выпадет число : {win}')
enter=input('Правила просты:\nЕсли ты считаешь, что заданное число выпадет следущим пиши букву: С(рус) \n  Сыграем?(да/нет) ')
for i in range(1000):
	if enter=='нет' or enter=='Нет':break
	numb=randint(1,10)
	print(i,'.', numb)
	enter=input("")
	if enter=="С" or enter=='с':
		numb=randint(1,10)
		print(i+1,'. ', numb)
		if numb==win:
			enter=print('Вау! Это очень сложно.Поздравляю!')
			enter='нет'
		else:
			enter=input('Не повезло( Продолжим? ')
	else:continue

