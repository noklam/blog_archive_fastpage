def insertionSort(arr):
  
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
  
        key = arr[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
  
  
# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)



def insertion_sort(arr):
        
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        print('Outer', i, pos, cursor)
        while pos > 0 and arr[pos - 1] > cursor:
            print(i, pos, cursor)
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor

    return arr

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)