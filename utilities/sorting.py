class SortUtils:
    """
    Utility class for data organisation.
    Implementing Merge Sort algorithm (R5).

    Merge Sort was chosen for consistent time complexity across
    best-to-worst scenarios: O(n Log(n)), and O(n) space complexity.
    This performance is superior over O(n^2) worst time complexity
    of algorithms like Quick and Bubble sort
    """

    @staticmethod
    def merge_sort(data, key=None, reverse=False):
        """
        High level wrapper for performing the whole Merge Sort.

        :param data: The list of unsorted data
        :param key: A lambda function or a property reference
        (e.g., 'x.last_name')
        :param reverse: A flag to determine sorting order
        :return: A new sorted list of data
        """

        # Return a copy of the list immediately if it is too small
        if len(data) <= 1:
            return data.copy() if data else []

        # Defensive step: Make a copy to avoid modifying original
        data_copy = data.copy()


        def merge_sort_recursive(arr):
            """
            Step 1. The division phase.
            Function performing the first step of the Merge Sort
            algorithm by recursively splitting the original list
            into sub-lists of one element.
            """
            if len(arr) <= 1:
                return arr

            # Find a middle object to split the array
            mid = len(arr) // 2

            # Recursive calls to continue splitting the original list
            # to left and right halves
            left = merge_sort_recursive(arr[:mid])
            right = merge_sort_recursive(arr[mid:])

            # Call a merging function to produce a sorted list
            return merge(left, right)


        def merge(left, right):
            """
            Step 2. The merging phase.
            Function merging lists by comparing them against
            each other and producing a sorted list.

            :param left: list of 'left' objects
            :param right: list of 'right' objects
            :return: sorted list
            """
            # Initialize a list holder and iterables
            result = []
            i = j = 0

            # While both lists are not empty
            while i < len(left) and j < len(right):
                # Compare elements from both lists using keys
                if key:
                    left_val = key(left[i])
                    right_val = key(right[j])
                else:
                    left_val = left[i]
                    right_val = right[j]

                # Handle string comparison (case-insensitive)
                if isinstance(left_val, str) and isinstance(right_val, str):
                    left_val = left_val.lower()
                    right_val = right_val.lower()

                # Compare and add to result
                if ((left_val <= right_val and not reverse) or
                        (left_val >= right_val and reverse)):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            # Add remaining elements
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        # Initial call for the recursive function
        return merge_sort_recursive(data_copy)