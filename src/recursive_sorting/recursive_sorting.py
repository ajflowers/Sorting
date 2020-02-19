# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    a = 0
    b = 0

    while a < len(arrA) or b < len(arrB):
        if b == len(arrB) or (a < len(arrA) and arrA[a] < arrB[b]):
            merged_arr[a+b] = arrA[a]
            a += 1
        else:
            merged_arr[a+b] = arrB[b]
            b += 1

    
    return merged_arr

# print(merge([0,8,9],[3,5,7]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        cutoff = round(0.5*len(arr))
        arr1 = arr[:cutoff]
        arr2 = arr[cutoff:]
        arr = merge(merge_sort(arr1), merge_sort(arr2))
        # print(arr1)    
        # print(arr2)

    return arr
# merge_sort([4,6,8])

# print(merge_sort([8,6,7,5,3,0,9]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
