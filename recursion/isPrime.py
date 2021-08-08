def isPrime(number: int, number2=None) -> bool:
    temp = number - 1 if number2 is None else number2
    if number == 2:
        return True

    if temp == 1:
        return True
    if (number % temp) == 0:
        return False
    else:
        if temp == 1:
            return True

        return isPrime(number, temp - 1)


print(isPrime(3))
print(isPrime(4))
print(isPrime(78))
print(isPrime(113))
