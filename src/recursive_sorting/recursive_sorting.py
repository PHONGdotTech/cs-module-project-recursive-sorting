# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    index = 0
    # Your code here
    while len(arrA) != 0 and len(arrB) != 0:
        if arrA[0] > arrB[0]:
            merged_arr[index] = arrB[0]
            arrB.pop(0)
        else:
            merged_arr[index] = arrA[0]
            arrA.pop(0)
        index += 1
    
    if len(arrA) == 0 and len(arrB) != 0:
        while len(arrB) !=0:
            merged_arr[index] = arrB[0]
            arrB.pop(0)
            index += 1
    elif len(arrB) == 0 and len(arrA) != 0:
        while len(arrA) !=0:
            merged_arr[index] = arrA[0]
            arrA.pop(0)
            index += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        return merge(merge_sort(left), merge_sort(right))

    return arr

# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l=0, r=None):
    # Your code here
    if (l < r)

    return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):
#     # Your code here

#     return arr
