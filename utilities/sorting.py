class SortUtils:
    @staticmethod
    def merge_sort(data, key=None, reverse=False):

        if len(data) <= 1:
            return data.copy() if data else []

        # Make a copy to avoid modifying original
        data_copy = data.copy()

        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                # Get values to compare
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
                if (left_val <= right_val and not reverse) or (left_val >= right_val and reverse):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            # Add remaining elements
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        def merge_sort_recursive(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort_recursive(arr[:mid])
            right = merge_sort_recursive(arr[mid:])

            return merge(left, right)

        return merge_sort_recursive(data_copy)