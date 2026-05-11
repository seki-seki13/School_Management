from utilities.displaying import DisplayUtils
from utilities.searching import SearchUtils
from utilities.menu_print import print_crud_options
from utilities.input_validation import get_pers_data, validate_number

from services.admin_services import AdminService

admin_serv = AdminService()
disp = DisplayUtils()
searcher = SearchUtils()

# ======== ADMIN MENU ========
def run_admin_menu():
    actions = [1, 3, 4]

    while True:
        print_crud_options('Admin', actions)
        try:
            choice = validate_number('Action: ')

            if choice == len(actions) + 1:
                break

            actual_action = actions[choice - 1]

            match actual_action:
                case 1:  # View All
                    data = admin_serv.view_all_admins()
                    disp.print_admins(data)

                case 3:  # Find (Binary Search)
                    data = admin_serv.view_all_admins()
                    a_id = validate_number('Enter Admin ID to find: ')
                    found = searcher.binary_search(
                        data, a_id, 'admin_id')
                    if found:
                        disp.print_admins([found])
                    else:
                        print('[!] Admin not found.')

                case 4:  # Add
                    print('--- Adding Admin ---')
                    f, l, d, t, a, p, e = get_pers_data()
                    print('--- Login Details ---')
                    while True:
                        try:
                            un = input('Username(>5): ')
                            pw = input('Password(>12): ')
                            admin_serv.add_admin(f, l, d, t, a, p, e, un, pw)
                            break
                        except Exception as e:
                            print('[!] Invalid Login. Try again')

        except Exception as e:
            print(f"Invalid input or Error: {e}")