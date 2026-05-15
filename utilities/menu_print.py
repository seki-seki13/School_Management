def print_crud_options(entity, number_list):
    """
    Utility function for a dynamic menu options printing.

    :param entity: A name identifying the menu category
    (e.g., 'Student', 'Grade')
    :param number_list: A list of integers representing
    available actions
    :return: A printed block of available actions
    """
    # Specify labels for actions using dictionary's key-value pairs
    labels = {1: 'View All', 2: 'View My', 3: 'Find',
              4: 'Add New', 5: 'Update', 6: 'Delete'}

    # Display the menu header in uppercase for visual clarity
    print(f"\n--- {entity.upper()} MANAGEMENT ---")

    # Iterate through the action list and display available options
    # enumerate is used for user-friendly indexing starting from 1
    for i, num in enumerate(number_list, 1):
        print(f"{i}. {labels[num]} {entity}")

    # Always ensure a 'Return' option as the final choice
    print(f"{len(number_list) + 1}. Go Back")