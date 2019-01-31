'''
---Insertion sort in python---

    => Take the second element of the array and compare it with elements before it and insert
       it in the proper location.
'''
'''
    input to the function is array that needed to be sorted
'''

def insertion_sort(arr):

    for i in range(len(arr)):

        temp = arr[i]
        j = i-1

        while arr[j] > temp and j >= 0:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = temp

    return arr


input_ = input("Enter the elements of the Array: ").split(' ')
array = [int(num) for num in input_]
print(array)
sorted_arr = insertion_sort(array)
print("Sorted array: " + str(sorted_arr))