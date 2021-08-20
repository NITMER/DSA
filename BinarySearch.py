from typing import List, Union


def search(array: List, element: int) -> Union[int, None]:
    length = len(array)
    high = length - 1
    low = 0
    while low <= high:
        mid = (high + low) // 2
        if array[mid] == element:
            return mid
        if array[mid] > element:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    print(search([1, 2, 3, 4, 5, 6, 7], 5))
    print(search([10, 20, 30, 40], 5))
    print(search([22, 33, 45, 55, 654], 55))
