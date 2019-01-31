'''
    -----Bubble Sort-----
    In bubble sort first element is compared to second element and if first element
    is grater than second then swap the value.

    => Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.

    => Best Case Time Complexity: O(n). Best case occurs when array is already sorted.

    => Auxiliary Space: O(1)
'''

def bubble_sort(arr):

    for i in range(len(arr)-1):

        # Flag to check if the array is already sorted (For best case solution).

        is_swpd = False

        # traverse the array from 0 to
        # n-i-1. Swap if the element
        # found is greater than the
        # next element
        for j in range(len(arr)-i-1):

            if arr[j] > arr[j+1]:

                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

                is_swpd = True

        if is_swpd is False:
            break
    return arr


input_ = input("Enter the elements of the Array: ").split(' ')
array = [int(num) for num in input_]
print("Input: " + str(array))
sorted_arr = bubble_sort(array)
print("Sorted array: " + str(sorted_arr))