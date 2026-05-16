# Importing display, search and validation utilities
from utilities.displaying import DisplayUtils
from utilities.searching import SearchUtils
from utilities.menu_print import print_crud_options
from utilities.input_validation import get_pers_data, validate_number

# Importing service layer for administrative database operations
from services.admin_services import AdminService

# Importing a shared menu option
from menus.shared_menu_options import find_person_ui

# Initialising service and utility instances for global use in this module
admin_serv = AdminService()
disp = DisplayUtils()
searcher = SearchUtils()


def run_admin_menu():
    """
    Manage the list of administrative accounts.
    Utilises a loop for continuous execution and
    employs match-case logic for operation routing.
    """
    # Define allowed action IDs: 1 (View), 3 (Find), 4 (Add)
    actions = [1, 3, 4]

    while True:
        # Generate the dynamic CRUD menu based on the allowed actions
        print_crud_options('Admin', actions)

        try:
            choice = validate_number('Action: ')

            # Break the loop to return to the previous menu
            if choice == len(actions) + 1:
                break

            # Identify the specific action ID based on user selection
            actual_action = actions[choice - 1]

            match actual_action:
                case 1:  # View All
                    data = admin_serv.view_all_admins()
                    disp.print_admins(data)

                case 3:  # Find (Binary Search)
                    find_person_ui('Admin')

                case 4:  # Add
                    print('--- Adding Admin ---')

                    # Collect validated personal details
                    f, l, d, t, a, p, e = get_pers_data()

                    print('--- Login Details ---')

                    while True:
                        try:
                            un = input('Username(>5): ')
                            pw = input('Password(>12): ')

                            # Pass input to the service
                            admin_serv.add_admin(f, l, d, t, a, p, e, un, pw)
                            break

                        except Exception as e:
                            print(f'[!] Invalid Login: {e}')

        # Unexpected errors handled with try-except
        except Exception as e:
            print(f'[!] Invalid input or Error: {e}')