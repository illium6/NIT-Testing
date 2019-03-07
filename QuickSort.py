import random

def reversed_quick_sort(Array, start_point, ArrayLen_m1):
    if start_point >= ArrayLen_m1:
        return
    else:
        q = random.choice(Array[start_point:ArrayLen_m1 + 1])
        i = start_point
        j = ArrayLen_m1
        while i <= j:
            while Array[i] > q:
                i += 1

            while Array[j] < q:
                j -= 1

            if i <= j:
                Array[i], Array[j] = Array[j], Array[i]
                i += 1
                j -= 1
                reversed_quick_sort(Array, start_point, j)
                reversed_quick_sort(Array, i, ArrayLen_m1)


def quick_sort(Array, start_point, ArrayLen_m1):
    if start_point >= ArrayLen_m1:
        return
    else:
        q = random.choice(Array[start_point:ArrayLen_m1 + 1])
        i = start_point
        j = ArrayLen_m1
        while i <= j:
            while Array[i] < q:
                i += 1

            while Array[j] > q:
                j -= 1

            if i <= j:
                Array[i], Array[j] = Array[j], Array[i]
                i += 1
                j -= 1
                quick_sort(Array, start_point, j)
                quick_sort(Array, i, ArrayLen_m1)

if __name__ == "__main__":
    
    array_len = 0
    array = []
    even_array = []
    odd_array = []

    with open("Input.txt", "r", encoding='utf-8') as input_file:
        array_len = int(input_file.read(2))
        array = input_file.read().split(' ')
    
    for i in range(array_len):
        array[i] = int(array[i])
        if array[i] % 2 == 0:
            even_array.append(array[i])
        else:
            odd_array.append(array[i])
    
    quick_sort(even_array, 0, len(even_array) - 1)
    reversed_quick_sort(odd_array, 0, len(odd_array) - 1)

    array = even_array + odd_array
    
    with open("Output.txt", 'w', encoding='utf-8') as output_file:
        for i in range(len(even_array)):
            output_file.write('%s ' % even_array[i])
        for i in range(len(odd_array)):
            output_file.write('%s ' % odd_array[i])

    print('Done!')
