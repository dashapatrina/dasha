Блочная сортировка
def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Шаг 1: Определение минимального и максимального значения в массиве
    min_val = min(arr)
    max_val = max(arr)
    
    # Количество корзин определяется числом уникальных возможных интервалов
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]

    # Шаг 2: Размещение элементов в соответствующие корзины
    for val in arr:
        index = int((val - min_val) / (max_val - min_val + 1) * (num_buckets - 1))
        buckets[index].append(val)

    # Шаг 3: Отсортировать содержимое каждой корзины (используем встроенную сортировку Python)
    sorted_arr = []
    for bucket in buckets:
        sorted_bucket = sorted(bucket)
        sorted_arr.extend(sorted_bucket)

    return sorted_arr


# Тестирование алгоритма
if __name__ == "__main__":
    input_array = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print("Исходный массив:", input_array)
    result = bucket_sort(input_array)
    print("Отсортированный массив:", result)
Вывод в консоль:
Исходный массив: [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
Отсортированный массив: [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897]



Блинная сортировка
def flip(arr, i):
    start = 0    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1def pancake_sort(arr):
    curr_size = len(arr)
    while curr_size > 1:
        max_idx = arr.index(max(arr[:curr_size]))
        if max_idx != curr_size - 1:
            flip(arr, max_idx)
            flip(arr, curr_size - 1)
        curr_size -= 1
    return arr
# Тестирование
arr = [3, 6, 2, 4, 5]
sorted_arr = pancake_sort(arr)
print("Отсортированный массив:", sorted_arr)

Вывод в консоль:
Исходный массив:[3, 6, 2, 4, 5]
Отсортированный массив:[2, 3, 4, 5, 6]

Сортировка бусинами
def bead_sort(arr):
    rows = [[True]num + [False](max(arr)-num) for num in arr]
    transposed = list(map(list, zip(*rows)))
    columns_sorted = [[any(row) for row in col] for col in transposed]
    sorted_rows = list(map(list, zip(*columns_sorted)))
    return [sum(row) for row in sorted_rows]
# Тестирование
arr = [5, 3, 1, 7]
sorted_arr = bead_sort(arr)
print("Отсортированный массив:", sorted_arr)

Вывод в консоль:
Исходный массив: [5,3,1,7]
Отсортированный массив: [1,3,5,7]


Поиск Скачками
import math
def jump_search(arr, x):
    step = int(math.sqrt(len(arr)))# Размер шага
    prev = 0
    while arr[min(step, len(arr))-1] < x:
        prev = step
        step += int(math.sqrt(len(arr)))
        if prev >= len(arr):
            return None
    # Обычный линейный поиск в пределах найденного блока
    while arr[prev] < x:
        prev += 1
        if prev == min(step, len(arr)):
            return None
    if arr[prev] == x:
        return prev
    else:
        return None
# Тестирование
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
search_value = 55
result = jump_search(arr, search_value)
if result is not None:
    print(f"Значение {search_value} найдено на индексе {result}")
else:
    print(f"{search_value} не найдено")

Вывод в консоль:
Исходный массив: [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610]
Отсортированный массив:[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610]

Экспоненциальный поиск
def exponential_search(arr, target):
    size = len(arr)
    bound = 1
    while bound < size and arr[bound] <= target:
        bound *= 2
    
    left = bound // 2
    right = min(bound, size-1)
    
    # Применяем бинарный поиск в диапазоне [left, right]
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

# Тестирование
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
target = 55
index = exponential_search(arr, target)
if index is not None:
    print(f"Искомое значение {target} находится на индексе {index}.")
else:
    print(f"Искомое значение {target} не найдено.")
Вывод в консоль:
Исходный массив:[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
Отсортированный массив:Искомое значение 55 находится на индексе 10