from services.room_service import RoomService
from utilities.displaying import DisplayUtils
from utilities.input_validation import validate_number, validate_input
from utilities.menu_print import  print_crud_options

room_serv = RoomService()
disp = DisplayUtils()

# === ROOMS SUBMENU (Rooms/Room Types Management)

def run_rooms_submenu():
    while True:
        print('\n-- ROOM SUBMENU --\n'
              '1. Rooms Management\n'
              '2. Room Types Management\n'
              '3. Go Back')
        choice = validate_number('Select: ')
        if choice == 1: rooms_management()
        elif choice == 2: room_types_management()
        elif choice == 3: break
        else: print('[!] Invalid choice.')

def rooms_management():
    actions = [1, 4]

    while True:
        print_crud_options('Room', actions)
        try:
            choice = validate_number('Action: ')

            if choice == len(actions) + 1:
                break

            actual_action = actions[choice - 1]

            match actual_action:
                case 1:  # View
                    data = room_serv.view_rooms()
                    disp.print_rooms(data)

                case 4:  # Add
                    print('--- Adding Room ---')
                    disp.print_rooms_types(
                        room_serv.v_room_types())
                    l = validate_input('Room Label: ')
                    f = validate_number('Floor (1-5): ',
                                        1, 5)
                    c = validate_number('Capacity (1-200): ',
                                        1, 200)
                    t = validate_number('Type ID: ')
                    room_serv.add_room(l, f, c, t)
        except Exception as e:
            print(f"Invalid input or Error: {e}")

def room_types_management():
    actions = [1, 4]

    while True:
        print_crud_options('Room Type', actions)
        try:
            choice = validate_number('Action: ')

            if choice == len(actions) + 1:
                break

            actual_action = actions[choice - 1]

            match actual_action:
                case 1:  # View
                    data = room_serv.v_room_types()
                    disp.print_rooms_types(data)

                case 4:  # Add
                    print('--- Adding Room Type ---')
                    disp.print_rooms_types(
                        room_serv.v_room_types())
                    t = validate_input('Type Name: ')
                    room_serv.add_room_type(t)
        except Exception as e:
            print(f"Invalid input or Error: {e}")