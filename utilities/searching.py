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
        # 1. Binary Search ONLY works on sorted data.
        # We must ensure the list is sorted by the search attribute first.
        from utilities.sorting import SortUtils
        sorted_list = SortUtils.merge_sort(data_list, key=lambda x: str(getattr(x, attr_name)))

        low = 0
        high = len(sorted_list) - 1
        target = str(target_value).lower()

        while low <= high:
            mid = (low + high) // 2
            current_obj = sorted_list[mid]
            current_val = str(getattr(current_obj, attr_name)).lower()

            if current_val == target:
                return current_obj
            elif current_val < target:
                low = mid + 1
            else:
                high = mid - 1

        return None