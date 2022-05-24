array=[69,10,30,2,16,8,31,22]
def shell_sort(arr):
    N=len(arr)
    h= N//2
    while h>0:
        for i in range(h,N):
            temp = arr[i]
            j= i -h
            while j>= 0 and arr[j]>temp:
                arr[j+h] = arr[j]
                j-=h
            arr[j+h]=temp
        h//=2
    print("정렬 결과 출력")
    print(arr)
shell_sort(array)