def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                tmp = lst[j + 1]
                lst[j + 1] = lst[j]
                lst[j] = tmp


def bubble_sort1(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if lst[j] < lst[j - 1]:
                tmp = lst[j - 1]
                lst[j - 1] = lst[j]
                lst[j] = tmp


def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        for j in range(i, n):
            if lst[j] < lst[min_index]:
                min_index = j

        if min_index != i:
            tmp = lst[i]
            lst[i] = lst[min_index]
            lst[min_index] = tmp


def insertion_sort(lst):
    for i in range(1, len(lst)):
        tmp = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > tmp:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = tmp


##testing
lst = [6, 7, 3, 1, 9, 2, 4, 5, 8, 0]

# bubleSort(lst)
# bubleSort1(lst)
# selectionSort(lst)
insertion_sort(lst)
print(lst)
