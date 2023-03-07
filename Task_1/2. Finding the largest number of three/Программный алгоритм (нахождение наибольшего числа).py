a = int(input('Введите первое целое число: '))
b = int(input('Введите второе целое число: '))
c = int(input('Введите третье целое число: '))

m = a
if m < b:
    m = b
if m < c:
    m = c

print(m)
