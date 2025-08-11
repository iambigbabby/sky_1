def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Флаг для оптимизации (если нет перестановок, массив отсортирован)
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Тестируем сортировку
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Исходный массив:", numbers)
sorted_numbers = bubble_sort(numbers)
print("Отсортированный массив:", sorted_numbers)