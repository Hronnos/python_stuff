from random import *


def guess_the_number():
    n = -1
    scoring = 0
    x = randint(1, 100)
    while n != x:
        n = int(input("Угадай число от 1 до 100: "))
        if n > x:
            scoring += 1
            print('Слишком много, попробуйте еще раз')
        if n < x:
            scoring += 1
            print('Слишком мало, попробуйте еще раз')
        if n == x:
            scoring += 1
            print('Поздравляю, вы угадали!')
            if n < 5:
                print('Вы сделали {} попытки'.format(scoring))
            else:
                print('Вы сделали {} попыток'.format(scoring))
            break


guess_the_number()
