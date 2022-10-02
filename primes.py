"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    numbers = 3
    if number_of_primes > 0:
        list.append(2)
        while len(list) < number_of_primes:
            flag = False
            for i in range(2, numbers):
                if numbers % i == 0:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                list.append(numbers)
            numbers = numbers + 1
     else:
         raise ValueError()
    return list
