def print_crud_options(entity, number_list):
    labels = {1: 'View All', 2: 'View My', 3: 'Find',
              4: 'Add New', 5: 'Update', 6: 'Delete'}

    print(f"\n--- {entity.upper()} MANAGEMENT ---")
    for i, num in enumerate(number_list, 1):
        print(f"{i}. {labels[num]} {entity}")
    print(f"{len(number_list) + 1}. Go Back")