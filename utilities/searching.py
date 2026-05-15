# Importing a sorting utility
from utilities.sorting import SortUtils

class SearchUtils:
    """
    Utility class for searching through loaded data using
    Binary Search algorithm (R5).

    Binary Search was selected due to its consistent O(log(n)) time
    complexity and O(1) space complexity, which is superior to Linear
    Search's O(n) complexity for larger datasets.

    Important: Binary Search works only on sorted data. Therefore,
    the Merge Sort algorithm is used before the searching.
    """

    @staticmethod
    def binary_search(data_list, target_value, attr_name):
        """
        Perform a generic Binary Search on a list of objects.

        :param data_list: List of objects to search through
        :param target_value: The specific value to find
        :param attr_name: The property to check (e.g., 'student_id')
        :return: The matching object or None
        """
        # Necessary pre-sorting before implementation
        sorted_list = SortUtils.merge_sort(
            data_list, key=lambda x: str(getattr(x, attr_name)))

        # Define starting boundaries and case-insensitive target match
        low = 0
        high = len(sorted_list) - 1
        target = str(target_value).lower()

        # Keep searching while search window is valid
        while low <= high:
            mid = (low + high) // 2
            current_obj = sorted_list[mid]

            # Valid comparison with lowercase and getattr
            current_val = str(getattr(current_obj, attr_name)).lower()

            # Conditions to stop or continue searching
            # while adjusting the boundaries
            if current_val == target:
                return current_obj
            elif current_val < target:
                low = mid + 1
            else:
                high = mid - 1

        # Return None if no match found
        return None