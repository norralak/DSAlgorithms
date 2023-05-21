class LinearSearch:
    #Introduction to Data Structures and Algorithms
    """
        An algorithm is simply a set of specific tasks to solve a particular problem. It should return a result. 
        
        We measure the time complexity by the upperbound (worst case) using big O notation.

        We want them to be efficient and accurate.

    """
    def linearSearch(list, target):
        """
        Returns the index position of the target if found, else return None
        """
        for i in range(0, len(list)):
            if list[i] == target:
                return i
        return None    
    """
    This algorithm's worst case is checking every single value where the value is at the end (last index).
    Time complexity is O(n) since it grows with n
    """
    # Helper Function
    def verify(index):
        if index is not None:
            print("Target found at index", index)
        else:
            print("Target not found in list")
    

    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    target = 13
    verify(linearSearch(num, target))