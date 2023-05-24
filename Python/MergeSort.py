
"""
Sort given list in ascending order
Returns a sorted list
Divide: Find the midpoint
Conquer: Recursively sort the sublists 
Combine: Merge the sorted sublists
"""
    

    
def mergeSort(arr):
    
    def split(arr):
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        return left, right
    
    def merge(left, right):
        sol = []
        i = 0 
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sol.append(left[i])
                i += 1
            else:
                sol.append(right[j])
                j += 1
        print(left)
        print (right)
        while i < len(left):
            sol.append(left[i])
            i += 1

        while j < len(right):
            sol.append(right[j])
            j += 1      
            
        return sol
    
    # Base case
    if len(arr) <= 1:
        return arr
    
    else:
        left, right = split(arr)
        left = mergeSort(left)
        right = mergeSort(right)
    
    return merge(left, right)


listy = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
listy = mergeSort(listy)
print(listy)
