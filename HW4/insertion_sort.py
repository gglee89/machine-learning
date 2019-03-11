# Chapter 4
# Section 1
# Decrease-and-Conquer strategy
def InsertionSort(arr):
    for i in range(len(arr)):
        v = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > v:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = v
    return arr

# Input Array
inputArr = [5,8,4,9,2,1,3]
print(inputArr)

# Result Array
result = InsertionSort(inputArr)
print(result)

