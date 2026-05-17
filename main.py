import sys
# Importing the logic for authentication and role-based menus
from services.auth_service import AuthService
from menus.student import run_stud_menu
from menus.admin.admin import run_admin
from menus.teacher import run_teach_menu


def main():
    """
    Main function and the system's entry point.
    Handles the authentication loop,
    directs users to appropriate menus.

    Loop implemented for continuous program execution
    unless the user decides to quit (R9).
    """
    auth = AuthService()

    while True:
        print(f"\n{'='*40}")
        print(' SCHOOL MANAGEMENT SYSTEM LOGIN')
        print(f"{'='*40}\n")
        try:
            # Use strip() to remove spaces from the input
            username = input('Username: ').strip()
            password = input('Password: ').strip()

            # Attempt to authenticate the user
            session = auth.login(username, password)

            if session:
                # session is truthy only if login() returned a valid session object
                # Nested if/elif/else checks the role attribute to route the user
                if session.role == 'Student':
                    # Student role: redirect to student-only portal
                    print('Loading Student Menu...')
                    run_stud_menu(session)  # Pass session to carry user context
                elif session.role == 'Teacher':
                    # Teacher role: redirect to teacher-only portal
                    print('Loading Teacher Menu...')
                    run_teach_menu(session)
                elif session.role == 'Admin':
                    # Admin role: full system access portal
                    print('Loading Admin Menu...')
                    run_admin(session)
            else:
                # session is None/False — authentication failed
                ask_again = input('\nLogin failed.\nTry again?(y/n): ')
                # Convert to lowercase to accept both 'Y' and 'y'
                if ask_again.lower() != 'y':
                    print('Program exited.')
                    sys.exit()  # Terminate the program cleanly

        # Exceptions handling
        except KeyboardInterrupt:
            print('Interrupted from keyboard. Program exited.')
            sys.exit()

        except Exception as e:
            print(f"Invalid input or Error: {e}")


if __name__ == '__main__':
    # Execute the main loop function
    main()