# ITP-100 Software Design
# Student: Bailey Paschall
# Instructor: Redacted for Privacy
# Date given to class: April 8th, 2022
# Date of Submission: April 19th, 2022
# Description: This program will read and print information from the "file_records" file if last name matches a file.
# Input: User is asked to input student last name.
# Output: This program prints all user information for that specific student if students last name matches.
# Additional Comments: Intstructions provided in canvas.


file_records = open('file_records', 'r')
line = file_records.readline()
line = line.split
user_input = ''
emptyList = []
FALSE = False
MATCH = False
TRUE = True
i = 1



def main():
    global TRUE, FALSE, MATCH, i, emptyList, file_records, line, user_input

    print()
    user_input = input("Enter a last name to search: ")

    while i == 1:

        file_records = open('file_records', 'r')

        while not MATCH:

            line = file_records.readline()
            line = line.split()

            if line != emptyList:

                lastName = line[0].replace('[', '').replace(']', '').replace("'", '').replace(',', '').replace(' ', '')

                if user_input == lastName:
                    MATCH = TRUE
                    i = 0
                    break

                if user_input != lastName:
                    i = 1

            if not line:
                i = 0
                MATCH = FALSE
                break

        file_records.close()

    if not MATCH:
        print()
        print(user_input, "not found in Records.")
        print()
        i = 1
        MATCH = FALSE

    if MATCH:
        print()
        print("Success, Record Found.")
        print()
        print("Student ID: " + line[1].replace('[', '').replace(']', '').replace("'", '').replace(',', '').replace(' ', ''))
        print("First Name: " + line[2].replace('[', '').replace(']', '').replace("'", '').replace(',', '').replace(' ', ''))
        print("Last Name: " + line[0].replace('[', '').replace(']', '').replace("'", '').replace(',', '').replace(' ', ''))
        print("Student Age: " + line[3].replace('[', '').replace(']', '').replace("'", '').replace(',', '').replace(' ', ''))
        print("Student Address: " + line[4].replace('[', '').replace(']', '').replace("'", '').replace(',', '').replace(' ', ''))
        print("Student Phone Number: " + line[5].replace('[', '').replace(']', '').replace("'", '').replace(',', '').replace(' ', ''))
        i = 1
        MATCH = FALSE
        print()


if __name__ == '__main__':
    main()
