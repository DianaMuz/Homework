#36
# переводим человеческий возраст в собачий
# просим пользователя ввести возраст
age = int(input('Введите человеческий возраст: '))

# переводим в собачий возраст в диапазоне от 1 до 2 человеческих лет
if 0 < age < 3:
    age *= 10.5
    print('Возраст в собачьих годах:', age)
# переводим в собачий возраст, если введенный человеческий возраст больше 2-ух
elif age > 2:
    age *= 4
    print('Возраст в собачьих годах:', age)
# выводим сообщение о неверно введенном значении
else:
    print('Введено неверное значение')

#39
# определяем количество дней в месяце

# просим пользователя ввести название месяца
month_name = str(input('Введите название месяца: '))

# определяем количество дней в месяце
if month_name.lower() == 'февраль':
    print(f'В {month_name.lower()} 28 или 29 дней.')
elif month_name.lower() == 'апрель' or month_name.lower() == 'июнь':
    print(f'В {month_name.lower()} 30 дней.')
elif month_name.lower() == 'сентябрь' or month_name.lower() == 'ноябрь':
    print(f'В {month_name.lower()} 30 дней.')
else:
    print(f'В {month_name.lower()} 31 день.')

#42
# преобразование названия ноты в частоту
C4_frequancy = 261.63
D4_frequancy= 293.66
E4_frequancy = 329.63
F4_frequancy = 349.23
G4_frequancy = 392.00
A4_frequancy = 440.00
B4_frequancy = 493.88
error = False

# просим пользователя ввести название ноты в виде буквы и цифры
note_name = input('Введите название ноты в виде буквы и цифры: ')
# приводим введенную пользователем строку к верхнему регистру
note_name = note_name.upper()

# название ноты и номер октавы сохраняем в разных переменных
note = note_name[0]
octave = int(note_name[1])

# находим частоту ноты в четвертой октаве
if note == 'C':
    freq = C4_frequancy
elif note == 'D':
    freq = D4_frequancy
elif note == 'E':
    freq = D4_frequancy
elif note == 'F':
    freq = F4_frequancy
elif note == 'G':
    freq = G4_frequancy
elif note == 'A':
    freq = G4_frequancy
elif note == 'B':
    freq = B4_frequancy
else:
    freq = error

# находим частоту ноты в конкретной октаве
freq = freq / 2 ** (4 - octave)

# выводим результат программы
if freq == error:
    print('Введено неверное значение.')
else:
    print(f'Частота ноты {note_name} равна {freq}')

#43
# определяем название ноты по введенной пользователем частоте
C4_frequancy = 261.63
D4_frequancy= 293.66
E4_frequancy = 329.63
F4_frequancy = 349.23
G4_frequancy = 392.00
A4_frequancy = 440.00
B4_frequancy = 493.88
error = False
lim = 1

# просим пользователя ввести частоту ноты
freq = float(input('Введите частоту ноты в Гц: '))

# определяем ноту по частоте. Если такой ноты нет, присваиваем булевое значение False
if (freq >= C4_frequancy - lim) and (freq <= C4_frequancy + lim):
    note = 'C4'
elif (freq >= D4_frequancy - lim) and (freq <= D4_frequancy + lim):
    note = 'D4'
elif (freq >= E4_frequancy - lim) and (freq <= E4_frequancy + lim):
    note = 'E4'
elif (freq >= F4_frequancy - lim) and (freq <= F4_frequancy + lim):
    note = 'F4'
elif (freq >= G4_frequancy - lim) and (freq <= G4_frequancy + lim):
    note = 'G4'
elif (freq >= A4_frequancy - lim) and (freq <= A4_frequancy + lim):
    note = 'A4'
elif (freq >= B4_frequancy - lim) and (freq <= B4_frequancy + lim):
    note = 'B4'
else:
    note = error

# выводим результат программы
if note == error:
    print('Ноты с введенной частотой не существует. Попробуйте еще раз.')
else:
    print('Введенная частота соответствует ноте', note)

#49
# программа определяет животное по китайскому календарю по введенному пользователем году
# просим пользователя ввести год
birth_year = int(input('Введите год рождения: '))

# определяем животное по введенному году
if (birth_year - 2000) % 12 == 0:
    sign = 'Дракон'
elif (birth_year - 2000) % 12 == 0:
    sign = 'Змея'
elif (birth_year - 2000) % 12 == 0:
    sign = 'Лошадь'
elif (birth_year - 2000) % 12 == 0:
    sign = 'Коза'
elif (birth_year - 2000) % 12 == 0:
    sign = 'Обезьяна'
elif (birth_year - 2000) % 12 == 0:
    sign = 'Петух'
elif (birth_year - 2000) % 12 == 0:
    sign = 'Собака'
elif (birth_year - 2000) % 12 == 0:
    sign = 'Свинья'
elif (birth_year - 2000) % 12 == 0:
    sign = 'Крыса'
elif (birth_year - 2000) % 12 == 0:
    sign = 'Бык'
elif (birth_year - 2000) % 12 == 0:
    sign = 'Тигр'
else:
    sign = 'Кролик'

# выводим результат программы
print('Ваш знак зодиака по китайскому гороскопу:', sign)

#52
# программа переводит буквенные оценки в числовые
A = 4.0
A_plus = 4.0
A_minus = 3.7
B = 3.0
B_plus = 3.3
B_minus = 2.7
C = 2.0
C_plus = 2.3
C_minus = 1.7
D = 1.0
D_plus = 1.3
F = 0
error = False

# просим пользователя ввести буквенную оценку
letter_mark = input('Введите буквенную оценку: ')
# приводим введенную пользователем строку к верхнему регистру
letter_mark = letter_mark.upper()

# преобразуем буквенную оценку в числовую. Если введено неверное значение, присваиваем булевое значение False
if letter_mark == 'A+' or letter_mark == 'A':
    grade = A
elif letter_mark == 'A-':
    grade = A_minus
elif letter_mark == 'B+':
    grade = B_plus
elif letter_mark == 'B':
    grade = B
elif letter_mark == 'B-':
    grade = B_minus
elif letter_mark == 'C+':
    grade = C_plus
elif letter_mark == 'C':
    grade = C
elif letter_mark == 'C-':
    grade = C_minus
elif letter_mark == 'D+':
    grade = D_plus
elif letter_mark == 'D':
    grade = D
elif letter_mark == 'F':
    grade = F
else:
    grade = error

# выводим результат программы
if grade == error:
    print('Введено неправильное значение.')
else:
    print('Оценка', letter_mark, 'в баллах:', grade)

#75
# является ли введенная строка палиндромом

# просим пользователя ввести строку
word = input('Введите слово: ')

# пусть введенная строка полиндром
is_palindrom = True

# сравниваем символы с двух концов. Делаем, пока не дойдем до середины
i = 0
while i < len(word) / 2 and is_palindrom:
    # если символы не равны, это не палтндром
    if word[i] != word[len(word) - 1 - i]:
        is_palindrom = False
    # берем следующий символ строки
    i += 1

# выводим результат программы
if is_palindrom:
    print('Слово', word, '- палиндром.')
else:
    print('Слово', word, '- не палиндром.')

77
программа выводит таблицу умножения от 1 до 10
min_value = 1
max_value = 10

for i in range(min_value, max_value + 1):
    for j in range(min_value, max_value + 1):
        print(i * j)
    print()