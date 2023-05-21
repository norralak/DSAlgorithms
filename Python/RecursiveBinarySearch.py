class RecursiveBinarySearch:
    """
    Recursion is just something that calls itself:
        1. Identify a base case when the recursion stops
        2. Identify a recursion case
        3. Every time you create a sublist you allocate more memory. In this case, each recursion will divide the list by two
        4. Therefore, it is O(log(n)) space complexity 
    """
    
    def recursiveBinarySearch(self, lst, target, start=0):
        # Base Case
        if len(lst) == 0:
            return None

        mid = len(lst) // 2

        if lst[mid] == target:
            return start + mid
        elif lst[mid] > target:
            # Recursion
            return self.recursiveBinarySearch(lst[:mid], target, start)
        else: 
            # Recursion
            return self.recursiveBinarySearch(lst[mid+1:], target, start + mid + 1)   
    
    # Helper Function
    def verify(self, index):
        if index is not None:
            print("Target found at index", index)
        else:
            print("Target not found in list")

# Test the RecursiveBinarySearch class
rbSearch = RecursiveBinarySearch()
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
target = 13
rbSearch.verify(rbSearch.recursiveBinarySearch(num, target))
