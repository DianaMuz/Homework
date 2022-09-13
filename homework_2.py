#1
color_list = ['Красный', 'Зеленый', 'Белый', 'Черный', 'Розовый', 'Желтый'] #создаем список color_list с названиями цветов
color_list.pop(0)
color_list.pop(3)
color_list.pop(3)
print('1.', color_list)

#2
list_of_colors = ['Зеленый', 'Белый', 'Голубой', 'Желтый'] #создаем список list_of_colors с названием цветов на русском
list_of_colors_en = ['Green', 'White', 'Blue', 'Yellow']   #создаем список list_of_colors_en с названием цветов на англ
list_of_colors_updated = list_of_colors + list_of_colors_en #создаем новый объединенный список list_of_colors_updated
print('2.', list_of_colors_updated)

#3
timetable = {'day1': 'Monday', 'day2': 'Tuesday', 'activity_1': 'dancing', 'activity_2': 'swimming'} #создаем словарь timetable
print('3.', timetable.items()) #выводим пары ключ - значение

#001
name = input('001. Введите свое имя: ') #просим пользователя ввести имя
print(f'Hello, {name}!')

#002
person_name = input('002. Введите свое имя: ') #просим пользователя ввести имя
surname = input('Введите свою фамилию: ') #просим пользователя ввести фамилию
print(f'Hello, {person_name} {surname}!')

#003
print('003. \nWhat do you call a bear whith no teeth? \nA Gummy bear!') #выводим сообщение в две строчки

#004
first_num = int(input('004.\nВведите первое число: ')) #просим пользователя ввести первое число
second_num = int(input('Введите второе число: ')) #просим пользователя ввести второе число
print('The total is', first_num + second_num) #считаем сумму чисел

#005
first_number = int(input('005.\nВведите первое число: ')) #просим пользователя ввести первое число
second_number = int(input('Введите второе число: ')) #просим пользователя ввести второе число
third_number = int(input('Введите третье число: ')) #просим пользователя ввести третье число
print('The answer is', (first_number + second_number) * third_number)

#006
total_pizza_slice = int(input('006.\nСколько всего кусков пиццы у Вас было?\n')) #просим пользователя ввести общее число кусков пиццы
eaten_pizza_slices = int(input('Сколько кусков пиццы Вы съели? \n')) #просим пользователя ввести количество съеденныъ кусков
print(f'У Вас осталось {total_pizza_slice - eaten_pizza_slices} кусков пиццы.') #выводим оставшееся число кусков пиццы

#007
persons_name = input('007.\nВведите свое имя: ') #просим пользователя ввести имя
persons_age = int(input('Введите свой возраст: ')) #просим пользователя ввести свой возраст
print(f'{persons_name}, next birthday you will be {persons_age}.')

#008
total_bill = int(input('008.\nВведите общую сумму счета за вечер: ')) #просим пользователя ввести общую сумму счета
amount_of_people = int(input('Введите количество людей на ужине ')) #просим пользователя ввести количество людей
print(f'Каждый должен заплатить {total_bill // amount_of_people} руб.') #выводим счет на одного человека

#009
day_number = int(input('009.\nВведите любое количество дней: ')) #просим аользователя ввести число в дня
print(f'В {day_number} днях: {day_number * 24} часов, {day_number * 1440} минут и {day_number * 86400} секунд.')

#010
weight_into_ft = int(input('010.\nВведите вес в кг: ')) #просим подьзователя ввести вес в кг
print(f'{weight_into_ft} кг - {weight_into_ft * 2.204} в фунтах.') #выводим вес в фунтах

#011
number_over_100 = int(input('011.\nВведите число больше 100: ')) #просим пользователя ввести число больше 100
number_lower_10 = int(input('Введите число меньше 10: ')) #просим пользователя ввести число меньще 10
print(f'В {number_over_100} число {number_lower_10} помещается {number_over_100 // number_lower_10} раз.')
