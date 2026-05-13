from src.my_array import MyArray


def reverse_array(array: MyArray) -> MyArray:
    length = len(array)

    for i in range(length // 2):
        j = length - 1 - i

        temp = array[i]
        array[i] = array[j]
        array[j] = temp

    return array

