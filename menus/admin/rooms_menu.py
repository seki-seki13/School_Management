# Importing service layer for classroom and infrastructure operations
from services.room_service import RoomService
# Importing utilities for data display, input validation, and menu formatting
from utilities.displaying import DisplayUtils
from utilities.input_validation import validate_number, validate_input
from utilities.menu_print import print_crud_options

# Initialising service and display instances
room_serv = RoomService()
disp = DisplayUtils()


def run_rooms_submenu():
    """
    Manage the room routing menu.
    Allows administrators to navigate between specific classroom
    management and the definition of room categories (types).
    """

    while True:
        print('\n-- ROOM SUBMENU --\n'
              '1. Rooms Management\n'
              '2. Room Types Management\n'
              '3. Go Back')
        choice = validate_number('Select: ')

        # Redirection to chosen submenus
        # if-else structure for choice routing
        if choice == 1: rooms_management()
        elif choice == 2: room_types_management()
        elif choice == 3: break # Go back to main admin menu
        else: print('[!] Invalid choice.')


def rooms_management():
    """
    Manage rooms menu.
    Supports viewing current inventory and adding new classroom data
    with associated constraints.
    """
    # Define allowed actions: 1 (View), 4 (Add)
    actions = [1, 4]

    while True:
        # Generate the dynamic CRUD menu based on the allowed actions
        print_crud_options('Room', actions)

        try:
            choice = validate_number('Action: ')

            # Break the loop to return to the previous menu
            if choice == len(actions) + 1:
                break

            # Identify the specific action ID based on user selection
            actual_action = actions[choice - 1]

            match actual_action:
                case 1:  # View
                    data = room_serv.view_rooms()
                    disp.print_rooms(data)

                case 4:  # Add
                    print('--- Adding Room ---')
                    # Display existing room types for UX
                    disp.print_rooms_types(
                        room_serv.v_room_types())

                    # Collect valid inputs
                    l = validate_input('Room Label: ')
                    f = validate_number('Floor (1-5): ',
                                        1, 5)
                    c = validate_number('Capacity (1-200): ',
                                        1, 200)
                    t = validate_number('Type ID: ')

                    # Pass inputs into service
                    room_serv.add_room(l, f, c, t)

        # Unexpected errors handled with try-except
        except Exception as e:
            print(f"Invalid input or Error: {e}")

def room_types_management():
    actions = [1, 4]

    while True:
        print_crud_options('Room Type', actions)
        try:
            choice = validate_number('Action: ')

            # Break the loop to return to the previous menu
            if choice == len(actions) + 1:
                break

            # Identify the specific action ID based on user selection
            actual_action = actions[choice - 1]

            match actual_action:
                case 1:  # View
                    data = room_serv.v_room_types()
                    disp.print_rooms_types(data)

                case 4:  # Add
                    print('--- Adding Room Type ---')
                    # Display existing room types for UX
                    disp.print_rooms_types(
                        room_serv.v_room_types())

                    t = validate_input('Type Name: ')
                    room_serv.add_room_type(t)

        # Unexpected errors handled with try-except
        except Exception as e:
            print(f"Invalid input or Error: {e}")