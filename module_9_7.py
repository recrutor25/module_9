#!/home/igor/PycharmProjects/module_9/.venv/bin/python
# -*- coding: utf-8 -*-


def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        for i in range(2, int(res ** 0.5 + 1)):
            if res % i == 0:
                print("Составное")
                break
        else:
            print('Простое')
        return res

    return wrapper


@is_prime
def sum_3(*args: int):
    return sum(args)


result = sum_3(2, 3, 6)
print(result)