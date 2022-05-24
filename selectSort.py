array=[69,10,30,2,16,8,31,22]
temp = 0;
def selectSort(array):
    print("정렬할원소 ",array)
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]>array[j]:
                temp=array[i]
                array[i] = array[j]
                array[j]=temp

    print(array)

selectSort(array)