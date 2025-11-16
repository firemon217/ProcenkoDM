

def bubble_sort(arr):
    """
    Bubble Sort
    Лучший случай:     O(n)        — если массив уже отсортирован
    Средний случай:    O(n^2)
    Худший случай:     O(n^2)
    Память:            O(1)        — сортировка на месте
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def insertion_sort(arr):
    """
    Insertion Sort
    Лучший случай:     O(n)        — почти отсортированный массив
    Средний случай:    O(n^2)
    Худший случай:     O(n^2)
    Память:            O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr

def selection_sort(arr):
    """
    Selection Sort
    Лучший случай:     O(n^2)
    Средний случай:    O(n^2)
    Худший случай:     O(n^2)
    Память:            O(1)
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def merge_sort(arr):
    """
    Merge Sort
    Лучший случай:     O(n log n)
    Средний случай:    O(n log n)
    Худший случай:     O(n log n)
    Память:            O(n)        — требует дополнительный массив
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    
    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    return merge(left, right)


def quick_sort(arr):
    """
    Quick Sort
    Лучший случай:     O(n log n)
    Средний случай:    O(n log n)
    Худший случай:     O(n^2)      — если pivot выбран неудачно
    Память:            O(log n)    — глубина рекурсии
    """
    def _quick_sort(a, low, high):
        if low < high:
            p = partition(a, low, high)
            _quick_sort(a, low, p - 1)
            _quick_sort(a, p + 1, high)

    def partition(a, low, high):
        pivot = a[high]
        i = low
        for j in range(low, high):
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[high] = a[high], a[i]
        return i

    _quick_sort(arr, 0, len(arr) - 1)
    return arr