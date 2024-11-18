def arithmetic_sequence(a0, d):
    a = a0
    while True:
        yield a
        a += d
'''
# Вызов функции и вывод первых 50 значений
sequence = arithmetic_sequence(-0.5, 0.1)
for i, value in enumerate(sequence):
    if i < 50:
        print(value)
    else:
        break
'''