array=[69,10,30,2,16,8,31,22]
def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
    print("삽입 정렬 수행")
    print(arr)
insertion_sort(array)
