def fact(number: int) -> int:
    if number <= 1:
        return 1
    else:
        return number * fact(number - 1)


print(fact(5))
