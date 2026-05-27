def print_crud_options(entity, number_list):
    """
    Utility function for dynamic menu option printing.
    :param entity: Menu category name (e.g., 'Student', 'Grade')
    :param number_list: List of integers representing available actions
    :return: Printed block of available actions
    """
    # Dictionary maps action IDs to human-readable labels
    # Key = action ID, Value = display label
    labels = {1: 'View All', 2: 'View My', 3: 'Find',
              4: 'Add New', 5: 'Update', 6: 'Delete'}

    # Header printed in uppercase for visual separation
    print(f"\n--- {entity.upper()} MANAGEMENT ---")

    # for loop iterates over number_list
    # enumerate() adds a counter starting at 1 for display numbering
    # i = display index (1, 2, 3...), num = actual action ID
    for i, num in enumerate(number_list, 1):
        print(f"{i}. {labels[num]} {entity}")

    # Go Back is always appended as the last option
    # len() + 1 ensures it follows the last numbered action
    print(f"{len(number_list) + 1}. Go Back")

