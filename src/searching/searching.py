# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    if end >= start:

        # Finding the center of the "new" array
        mid = (start + end) // 2

        # If the middle of the array has the target, return the middle index.
        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, end)
        else:
            return binary_search(arr, target, start, mid - 1)
    else:
        return -1

    # STRETCH: implement an order-agnostic binary search
    # This version of binary search should correctly find
    # the target regardless of whether the input array is
    # sorted in ascending order or in descending order
    # You can implement this function either recursively
    # or iteratively


# def agnostic_binary_search(arr, target):
#     # Your code here
