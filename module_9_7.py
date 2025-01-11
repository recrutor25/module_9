#!/home/igor/PycharmProjects/module_9/.venv/bin/python
# -*- coding: utf-8 -*-
def is_prime(func):
    def wrapper(*args):
        summa = func(*args)
        is_prime = True
        if summa > 1:
            for i in range(2, (summa//2)+1):
                if summa % i == 0:
                 is_prime = False
            if is_prime == True:
                return (f'Простое\n{summa}')

            else:
                return (f'Составное\n{summa}')

    return wrapper

@is_prime
def sum_three(*args: int):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)

