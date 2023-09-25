# ITP-100 Software Design
# Student: Bailey Paschall
# Instructor: Redacted for Privacy
# Date given to class: April 8th, 2022
# Date of Submission: April 19th, 2022
# Description: This program will display a menu for the user. It will display 1 - 5 options, 4 of which requiring further user input.
# Input: User is asked to input numbers 1 through 5. Create, Show, Delete, or Display Record.
# Output: This program outputs the main function of another program if applicable, option 5 exits menu and terminates program.
# Additional Comments: Intstructions provided in canvas.


CREATE_NEW_RECORD = 1
SHOW_A_RECORD = 2
DELETE_A_RECORD = 3
DISPLAY_ALL_RECORDS = 4
EXIT = 5


def main():
    global DISPLAY_ALL_RECORDS
    global CREATE_NEW_RECORD
    global DELETE_A_RECORD
    global SHOW_A_RECORD
    global EXIT

    menuLaunchInput = input("Press Enter to Launch Menu ")
    print()

    if menuLaunchInput.upper() == '':
        i = 1

        display_menu()
        choice = int(input("Enter your option [1 - 5]: "))

        while i >= 1:

            if choice == CREATE_NEW_RECORD:
                from CreateRecord import main
                print()
                print("You chose option ", CREATE_NEW_RECORD, "... Preparing to create a new record. \n", sep='', end='')
                main()
                userMenuInput = input("Press enter to bring up menu. ")
                print()
                if userMenuInput == '':
                    display_menu()
                    choice = int(input("Enter your option [1 - 5]: "))
                    i = 1
                if userMenuInput != '':
                    print("Menu closing.")
                    i = 0

            elif choice == SHOW_A_RECORD:
                from ShowRecord import main
                print()
                print("You chose option ", SHOW_A_RECORD, "... Preparing to show a new record. \n", sep='', end='')
                main()
                userMenuInput = input("Press enter to bring up menu. ")
                print()
                if userMenuInput == '':
                    display_menu()
                    choice = int(input("Enter your option [1 - 5]: "))
                    i = 1
                if userMenuInput != '':
                    print("Menu closing.")
                    i = 0

            elif choice == DELETE_A_RECORD:
                from DeleteRecord import main
                print()
                print("You chose option ", DELETE_A_RECORD, "... Preparing to delete a record. \n", sep='', end='')
                main()
                userMenuInput = input("Press enter to bring up menu. ")
                print()
                if userMenuInput == '':
                    display_menu()
                    choice = int(input("Enter your option [1 - 5]: "))
                    i = 1
                if userMenuInput != '':
                    print("Menu closing.")
                    i = 0

            elif choice == DISPLAY_ALL_RECORDS:
                from DisplayRecords import main
                print()
                print("You chose option ", DISPLAY_ALL_RECORDS, "... Preparing to display all records. \n", sep='', end='')
                main()
                userMenuInput = input("Press enter to bring up menu. ")
                print()
                if userMenuInput == '':
                    display_menu()
                    choice = int(input("Enter your option [1 - 5]: "))
                    i = 1
                if userMenuInput != '':
                    print("Menu closing.")
                    i = 0

            elif choice == EXIT:
                print()
                print("You chose option ", EXIT, "... Exiting menu. \n", sep='', end='')
                i = 0

            else:
                print()
                print(choice, "is not an option listed in the menu. Restart Program. \n")
                break
    else:
        print("Wrong input. Run Program Again.")
        exit()


def display_menu():

    print("***************************")
    print('      RECORDS MANAGER      ')
    print("***************************")
    print()
    print('1) Create new record.')
    print('2) Show a record.')
    print('3) Delete a record.')
    print('4) Display all records.')
    print('5) Quit')
    print()


if __name__ == '__main__':
    main()
