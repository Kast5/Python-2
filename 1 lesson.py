# найти сумму и произведение цифр трехзначного числа которое вводит пользователь

number = input('Введите число: ')

sum = 0
prod = 1

for f in number:
    sum += int(f)
    prod *= int(f)
print(f"Сумма цифр числа {number}: {sum}")
print(f"Произведение цифр: {number}: {prod}")


# По введенным пользователем координатам двух точек вывести уравнение
# прямой вида y=kx+b, проходящей через эти точки.

x1, y1, x2, y2 = [
    int(x) for x in input('Введите кординаты (x1 y1 x2 y2): ').split()
]

k = (y2 - y1)/(x2 - x1)
b = y1 - k * x1

print(f'Уравнение прямой: y = {k}x + {b}')


# Пользователь вводит две буквы. Определить, на каких местах алфавита они
# стоят и сколько между ними находится букв.

letter1, letter2 = [
  x.upper() for x in input('Введите две буквы, через пробел (A - Z): ').split()
]

# Генерация списка букв
abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

index_letter1 = abc_list.index(letter1) + 1
index_letter2 = abc_list.index(letter2) + 1

if index_letter1 < index_letter2:
    step = 1
else:
    step = -1

print(f'Первая буква {letter1}, находится на позиции: {index_letter1}')
print(f'Вторая буква {letter2}, находится на позиции: {index_letter2}')

print(
    f'Между ними находятся буквы \
{abc_list[abc_list.index(letter1) + step:abc_list.index(letter2):step]} \
({abs(index_letter1 - index_letter2) - 1})'
)

# Пользователь вводит номер буквы в алфавите. Определить,
# какая это буква.
abc_number = int(input('Введите номер буквы в алфавите: '))

# Генерация списка букв
abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
print(abc_list)
if abc_number <= len(abc_list):
    print(f'Буква под номером {abc_number}: {abc_list[abc_number - 1]}')
else:
    print(
      f'Введено число превышающее количество букв в алфавите ({len(abc_list)})'
    )

# По длинам трех отрезков, введенных пользователем, определить возможность
# существования треугольника, составленного из этих отрезков. Если такой
# треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.

a, b, c = [
      float(x) for x in input('Введите длины отрезков, через пробел: ').split()
        ]

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print(f'Треугольник со сторонами {a} {b} {c} - равносторонний')
    elif a == b or b == c or c == a:
        print(f'Треугольник со сторонами {a} {b} {c} - равнобедренный')
    else:
        print(f'Треугольник со сторонами {a} {b} {c} - разносторонний')
else:
    print(f'Треугольника со сторонами {a} {b} {c} не существует')

# Вводятся три разных числа. Найти, какое из них является средним
# (больше одного, но меньше другого).

n1, n2, n3 = [x for x in input('Введите три числа, через пробел: ').split()]

if n2 < n1 < n3 or n3 < n1 < n2:
    print(f'Среднее: {n1}')
elif n1 < n2 < n3 or n3 < n2 < n1:
    print(f'Среднее: {n2}')
else:
    print(f'Среднее: {n3}')