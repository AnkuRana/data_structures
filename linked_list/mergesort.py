import sys
def mergesort(arr, l, r):
    if l < r:
        m = l + (r - l)//2
        
        mergesort(arr,l,m)
        mergesort(arr,m+1,r)
        
        merge(arr,l,r,m)

def merge(arr, l , r, m):
    larr = []
    rarr = []
    n1 = m - l + 1
    n2 = r - m
    for i in range(n1):
        larr.append(arr[l+i])
    for j in range(n2):
        rarr.append(arr[m+1+j])
    
    i = j = 0
    k = l
    while i < n1 and j < n2:
        if larr[i] <= rarr[j]:
            arr[k] = larr[i]
            i+=1
        else:
            arr[k] = rarr[j]
            j+=1
        k+=1
    
    while i < n1:
        arr[k] =larr[i]
        i+=1
        k+=1
    
    while j < n2:
        arr[k] = rarr[j]
        j+=1
        k+=1
# def mergeSort(arr):
#     if len(arr) > 1:
 
#          # Finding the mid of the array
#         mid = len(arr)//2
 
#         # Dividing the array elements
#         L = arr[:mid]
 
#         # into 2 halves
#         R = arr[mid:]
 
#         # Sorting the first half
#         mergeSort(L)
 
#         # Sorting the second half
#         mergeSort(R)
 
#         i = j = k = 0
 
#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i] <= R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
 
#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
 
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
 
arr = [1,3,2,6,5,8,4,9,7]
print(sys.getrecursionlimit())
# sys.setrecursionlimit(1500)
mergesort(arr,0,len(arr)-1)
print(arr)