import time


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Пример использования с измерением времени:
array = [12, 11, 13, 5, 6, 7]
start_time = time.time()
merge_sort(array)
end_time = time.time()
print("Отсортированный массив (слиянием):", array)
print("Время выполнения (слиянием):", end_time - start_time, "секунд")
