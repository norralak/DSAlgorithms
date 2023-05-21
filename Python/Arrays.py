class arraysRev:
    arr = [1, 2, 3, 4, 5, 6]
    """
    Above is an array
    They have indexes starting at zero
    When you insert from the front, it is more expensive because you're moving the rest up by 1 index
    This is a linear time complexity
    Appending is less expensive since it just adds an element to len(arr) index
    Delete operations is O(n) as well as the elements after the deleted have to be shifted
    """
    