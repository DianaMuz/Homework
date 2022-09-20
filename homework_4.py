#045
# создаем счетчик и присваиваем значение 0
total = 0

# создаем цикл, в котором просим пользователя ввести число, прибавляем это число к total
# цикл работает пока total <= 50 и выводит значение total
while total <= 50:
    number = int(input('Введите число: '))
    total += number
    print('The total is', total)

#046
number = 0
# просим пользователя вводить число, пока оно меньше 5
while number < 5:
    number = int(input('Введите число: '))
# если число больще 5, выводим результат
print('The last number you entered was', number)

#047
# просим пользователя ввести число
first_number = int(input('Введите число: '))

# присваиваем значение first_number в total
total = first_number
answer = 'y'

# пока ответ 'y', просим пользователя вводить число
while answer == 'y':
    new_number = int(input('Введите число: '))
    # ссумируем введенные пользователем числа
    total += new_number
    answer = input('Хотите ввести еще одно число? Ответьте y or n. ')
    answer = answer.lower()
# в результате выводим сумму всех введенных чисел
print('The total is', total)

#048
total = 0
answer = 'y'

# просим пользователя вводить имена гостей, пока его ответ 'y'
while answer == 'y':
    name = str(input('Введите имя гостя: '))
    # добавляем каждого нового гостя
    total += 1
    # выводим имя приглашенного гостя
    print(name, 'has been invited.')
    answer = input('Do you want to invite smb else? Answer y or n: ')
    answer = answer.lower()
# в результате выводим общее количество приглашенных гостей
print('You have invited', total, 'people to the party.')

#049
compnum = 50
# просим пользователя угадать задуманное число
number = int(input('Введите число, которое было задумано: '))
attempts = 1

# пока введенное пользователем число не равно 50 запускаем цикл
while number != compnum:
    # если число меньше 50
    if number < 50:
        print('Больше.')
    # если число больше 50
    else:
        print('Меньше.')
    # суммируем попытки пользователя и просим угадать число еще раз
    attempts += 1
    number = int(input('Попробуйте еще раз: '))
# в результате выводим за какое количество попыток было угадано число
print('Вы угадали! Вам потребовалось', attempts, 'попыток.')

#050
# просим пользователя ввести число от 10 до 20
number = int(input('Введите число от 10 до 20: '))

# запускаем цикл, пока введенное число меньше 10 или больше 20
while number < 10 or number > 20:
    # если число меньше 10
    if number < 10:
        print('Too low.')
    # если число больше 20
    else:
        print('Too high.')
    # просим ввести число еще раз
    number = int(input('Попробуйте еще раз: '))
# выводим результат
print('Thank you!')

#051
