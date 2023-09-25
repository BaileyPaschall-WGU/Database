# ITP-100 Software Design
# Student: Bailey Paschall
# Instructor: Redacted for Privacy
# Date given to class: April 8th, 2022
# Date of Submission: April 19th, 2022
# Description: This program will show records in ascending order.
# Input: User is not asked to input any information.
# Output: This program displays all records in ascending order.
# Additional Comments: Intstructions provided in canvas.


i = 1
emptyList = []


def main():

    global i, emptyList

    while i == 1:

        print()
        with open('file_records', 'r') as displayRecords:
            displayRecords = displayRecords.readlines()
            for line in sorted(displayRecords):
                print(line, end='')
                i = 0

        while displayRecords == emptyList:
            print('No records available. List is empty.')
            i = 1
            break
        print()

    while i == 0:
        print("Records successfully sorted.")
        print()
        i = 1
        break



if __name__ == '__main__':
    main()
