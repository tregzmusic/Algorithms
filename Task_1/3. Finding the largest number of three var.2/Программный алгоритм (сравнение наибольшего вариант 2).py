a = int(input('Введите первое целое число: '))
b = int(input('Введите второе целое число: '))
c = int(input('Введите третье целое число: '))

if a > b:
    if a > c:
        print(f'max = {a}')
    else:
        print(f'max = {c}')
else:
    if b > c:
        print(f'max = {b}')
    else:
        print(f'max = {c}')
