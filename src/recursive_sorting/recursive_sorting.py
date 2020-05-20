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
    start2 = mid + 1; 
  
    # If the direct merge is already sorted 
    if (arr[mid] <= arr[start2]): 
        return; 
      
    # Two pointers to maintain start 
    # of both arrays to merge 
    while (start <= mid and start2 <= end): 
  
        # If element 1 is in right place 
        if (arr[start] <= arr[start2]): 
            start += 1; 
        else: 
            value = arr[start2]; 
            index = start2; 
  
            # Shift all the elements between element 1 
            # element 2, right by 1. 
            while (index != start): 
                arr[index] = arr[index - 1]; 
                index -= 1; 
              
            arr[start] = value; 
  
            # Update all the pointers 
            start += 1; 
            mid += 1; 
            start2 += 1
    
    return arr


def merge_sort_in_place(arr, l=0, r=None):
    # Your code here
    if (l < r): 
  
        # Same as (l + r) / 2, but avoids overflow 
        # for large l and r 
        m = l + (r - l) // 2; 
  
        # Sort first and second halves 
        merge_sort_in_place(arr, l, m); 
        merge_sort_in_place(arr, m + 1, r); 
  
        merge_in_place(arr, l, m, r)

    return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):
#     # Your code here

#     return arr
