import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Пример использования с измерением времени:
array = [64, 34, 25, 12, 22, 11, 90]
start_time = time.time()
bubble_sort(array)
end_time = time.time()
print("Отсортированный массив (пузырьком):", array)
print("Время выполнения (пузырьком):", end_time - start_time, "секунд")
