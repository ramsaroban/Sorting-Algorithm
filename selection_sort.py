'''
    In selection sort, select an element from an array (from first or last) and compare it with other
    elements and swap if required.
    
    Time Complexity : O(n*2)
'''
'''
    INPUT: Array that needed to be sorted.
    OUTPUT: Sorted array
'''
def selection_sort(arr):
    
    for i in range(len(arr)):

        for j in range(i+1,len(arr)):

            if arr[i] > arr[j]:

                temp   = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr


input_ = input("Enter the elements of the Array: ").split(' ')
array = [int(num) for num in input_]
print("Input: " + str(array))
sorted_arr = selection_sort(array)
print("Sorted array: " + str(sorted_arr))
