def merge(A1,A2,arr):
    
    i = j = k = 0
    while i < len(A1) and j < len(A2):
        if A1[i] < A2[j]:
            arr[k] = A1[i]
            i += 1
        else:
            arr[k] = A2[j]
            j += 1
        k += 1
     
    while i < len(A1):
        arr[k] = A1[i]
        i += 1
        k += 1

    while j < len(A2):
        arr[k] = A2[j]
        j += 1
        k += 1

    return arr

def merge_sort(arr):
    
    if len(arr) > 1:
        mid = int(len(arr)//2)

        A1 = arr[:mid]
        A2 = arr[mid:]

        merge_sort(A1)
        merge_sort(A2)

        temp = merge(A1,A2,arr)
        return temp

input_ = input("Enter the elements of the Array: ").split(' ')
array = [int(num) for num in input_]
print("Input: " + str(array))
sorted_arr= merge_sort(array)
print("Sorted array: " + str(sorted_arr))
