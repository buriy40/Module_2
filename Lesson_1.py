import random

while True:
    target_number = random.randint(0,10)
    #print(target_number)
    endeavours = 3
    print('Угадай число от 1 до 10')
    for endeavour in range(1,endeavours+1):
        guess = int(input('введите число'))
        if guess == target_number:
            print('Верно!')
            break
        elif guess > target_number:
            print('Заданное число меньше')
        else:
            print('Заданное число больше')
        if endeavour == endeavours:
            print('Ты проиграл')

    play_agane = input('Еще разок? y/n ')
    if play_agane != 'y':
        print('Спасибо за игру!')




