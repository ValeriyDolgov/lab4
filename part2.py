import time


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Пример использования с измерением времени:
array = [64, 25, 12, 22, 11]
start_time = time.time()
selection_sort(array)
end_time = time.time()
print("Отсортированный массив (выбором):", array)
print("Время выполнения (выбором):", end_time - start_time, "секунд")
