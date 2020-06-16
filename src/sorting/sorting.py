# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    pointerA = 0
    pointerB = 0

    for i in range(elements):
        if pointerA == len(arrA):
            merged_arr[i] = arrB[pointerB]
            pointerB += 1
        elif pointerB == len(arrB):
            merged_arr[i] = arrA[pointerA]
            pointerA += 1
        elif arrA[pointerA] < arrB[pointerB]:
            merged_arr[i] = arrA[pointerA]
            pointerA += 1
        elif arrA[pointerA] > arrB[pointerB]:
            merged_arr[i] = arrB[pointerB]
            pointerB += 1
        else:
            merged_arr[i] = arrA[pointerA]
            pointerA += 1
            pointerB += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        leftArr = merge_sort(arr[0:len(arr)//2])
        rightArr = merge_sort(arr[len(arr)//2:])
        return merge(leftArr, rightArr)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    return -1

def merge_sort_in_place(arr, l, r):
    # Your code here
    return -1

