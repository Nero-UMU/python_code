import math


def primes(number):
    number += 1
    while True:
        sqrt = int(math.sqrt(number))
        for i in range(2, sqrt + 1):
            if number % i == 0:
                number += 1
            else:
                return number



number = int(input('请输入一个大于2的数：'))
prime = primes(number)
print(prime)