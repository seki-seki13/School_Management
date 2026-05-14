class SearchUtils:
    """
    Utility class for searching through loaded data.
    Requirement: Binary Search algorithm.
    """

    @staticmethod
    def binary_search(data_list, target_value, attr_name):
        """
        Generic Binary Search implementation.
        data_list: List of objects
        target_value: The value we are looking for
        attr_name: The property to check (e.g., 'student_id')
        """
        # Binary Search ONLY works on sorted data.
        # Utilising SortUtils is necessary to ensure correct
        # data organization before the searching process
        from utilities.sorting import SortUtils
        sorted_list = SortUtils.merge_sort(data_list, key=lambda x: str(getattr(x, attr_name)))

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