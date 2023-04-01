import sys
def quicksort(array,low,high):
    if low<high:
        pi = partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array, pi+1, high)
    return array
    
def partition(array, low, high):
    pivot = array[high]
    i = low -1
    for j in range(low,high):
        if array[j] <= pivot:
            i+=1
            swap(array,i ,j)
    swap(array ,i+1, high)
    return i+1

def swap(array,first, second):
    temp = array[first]
    array[first] = array[second]
    array[second] = temp
    
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
sys.setrecursionlimit(2000)
print (quicksort(test,0 ,len(test)-1))