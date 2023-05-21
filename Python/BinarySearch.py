class BinarySearch:
    """
    Here we'll find the target in a list given that it is sorted.
    The algorithm steps are, until the target is found:
        1. Find the midway value, compare it to the target
        2. If it's the target, return it
        3. Else, is it greater than or less than
        4. If greater, find midway value between the first index and current midway value
        5. If lesserm find midway value between current midway and max value 
    With this, since it is log2(n) (The inverse of n^2) **Think of it as you're decreasing the value by dividing two. n^2 is increasing by multiplying 2
    The time complexity is O(log(n))
    """
    def binarySearch(list, target):
        left = 0
        right = len(list) - 1

        while left <= right:
            mid = (left + right) // 2

            if list[mid] == target:
                return mid
            elif list[mid] > target:
                right = mid - 1
            elif list[mid] < target:
                left = mid + 1
        return None
        
     # Helper Function
    def verify(index):
        if index is not None:
            print("Target found at index", index)
        else:
            print("Target not found in list")
    

    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    target = 13
    verify(binarySearch(num, target))