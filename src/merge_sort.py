from src.my_array import MyArray


def merge_sort(array: MyArray) -> MyArray:
    
    array = [array[i] for i in range(len(array))]
    
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    esquerda_array = array[:mid]
    direita_array = array[mid:]

    esquerda_array = merge_sort(esquerda_array)
    direita_array = merge_sort(direita_array)

    result = []
    i = 0
    j = 0

    while i < len(esquerda_array) and j < len(direita_array):
        if esquerda_array[i] < direita_array[j]:
            result.append(esquerda_array[i])
            i += 1
        else:
            result.append(direita_array[j])
            j += 1

    result.extend(esquerda_array[i:])
    result.extend(direita_array[j:])

    return result
    

