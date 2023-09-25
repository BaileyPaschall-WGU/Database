# ITP-100 Software Design
# Student: Bailey Paschall
# Instructor: Redacted for Privacy
# Date given to class: April 8th, 2022
# Date of Submission: April 19th, 2022
# Description: This program will delete a record that matches the last name of the User Input
# Input: User is asked to input student last name of record they want deleted.
# Output: This program alerts the user once information has been deleted successfully.
# Additional Comments: Intstructions provided in canvas.


delete_user_input = ''
delCounter = 0
FALSE = False
FLAG = False
TRUE = True
i = 1


def main():

    global i, delCounter, delete_user_input

    i = 1

    while i == 1:

        print()
        delete_user_input = input("Enter the last name of the record you'd like to delete: ")

        with open("file_records", 'r') as file:
            lines = file.readlines()

        with open("file_records", 'w') as file:
            for line in lines:

                if line.find(delete_user_input) != -1:
                    pass
                    delCounter += 1
                else:
                    file.write(line)

        i = 0
        break

    if delCounter == 0:
        print()
        print("No files have been found with the last name '", delete_user_input, "'.", sep='')
        print()

    if delCounter >= 1:

        if delCounter == 1:
            print()
            print(delCounter, " file has been deleted with the last name '", delete_user_input, "'.", sep='')
            print()
            delCounter = 0

        if delCounter > 1:
            print()
            print(delCounter, " files have been deleted with the last name '", delete_user_input, "'.", sep='')
            print()
            delCounter = 0


if __name__ == '__main__':
    main()
