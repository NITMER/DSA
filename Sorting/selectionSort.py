from typing import List


def sort(array: List) -> List:
    for i in range(len(array) - 1):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
    return array


if __name__ == "__main__":
    print(sort([4, 5, 2, 32423, 45]))
    print(sort([426, 32, 234]))
    print(sort([200, 2007, 124312, 412412]))
