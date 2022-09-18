#36
age = int(input('Введите человеческий возраст: '))

if 0 < age < 3:
    age *= 10.5
    print('Возраст в собачьих годах:', age)
elif age > 2:
    age *= 4
    print('Возраст в собачьих годах:', age)
else:
    print('Введено неверное значение')

#39
month_name = str(input('Введите название месяца: '))

if month_name.lower() == 'февраль':
    print(f'В {month_name.lower()} 28 или 29 дней.')
elif month_name.lower() == 'апрель' or month_name.lower() == 'июнь':
    print(f'В {month_name.lower()} 30 дней.')
elif month_name.lower() == 'сентябрь' or month_name.lower() == 'ноябрь':
    print(f'В {month_name.lower()} 30 дней.')
else:
    print(f'В {month_name.lower()} 31 день.')

#42
C4_frequancy = 261.63
D4_frequancy= 293.66
E4_frequancy = 329.63
F4_frequancy = 349.23
G4_frequancy = 392.00
A4_frequancy = 440.00
B4_frequancy = 493.88
error = False

note_name = input('Введите название ноты в виде буквы и цифры: ')
note_name = note_name.upper()

note = note_name[0]
octave = int(note_name[1])

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

freq = freq / 2 ** (4 - octave)

if freq == error:
    print('Введено неверное значение.')
else:
    print(f'Частота ноты {note_name} равна {freq}')

#43
C4_frequancy = 261.63
D4_frequancy= 293.66
E4_frequancy = 329.63
F4_frequancy = 349.23
G4_frequancy = 392.00
A4_frequancy = 440.00
B4_frequancy = 493.88
error = False
lim = 1

freq = float(input('Введите частоту ноты в Гц: '))

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

if note == error:
    print('Ноты с введенной частотой не существует. Попробуйте еще раз.')
else:
    print('Введенная частота соответствует ноте', note)

#49
birth_year = int(input('Введите год рождения: '))

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
print('Ваш знак зодиака по китайскому гороскопу:', sign)

#52
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

letter_mark = input('Введите буквенную оценку: ')
letter_mark = letter_mark.upper()

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

if grade == error:
    print('Введено неправильное значение.')
else:
    print('Оценка', letter_mark, 'в баллах:', grade)
