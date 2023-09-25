# ITP-100 Software Design
# Student: Bailey Paschall
# Instructor: Redacted for Privacy
# Date given to class: April 8th, 2022
# Date of Submission: April 19th, 2022
# Description: This program will append text to the following .txt file; file_records
# Input: User is asked to input student information.
# Output: This program alerts the user once information has been written successfully.
# Additional Comments: Intstructions provided in canvas.


choice = 1


def main():
    global choice
    file_records = open("file_records", "a")

    if choice == 1:
        print()
        studentID = int(input("Enter the student ID: "))
        firstName = str(input("Enter the First Name: "))
        lastName = str(input("Enter the Last Name: "))
        studentAge = int(input("Enter the Age: "))
        studentAddress = str(input("Enter the Address: "))
        studentPhoneNumber = int(input("Enter the Phone Number: "))
        print()

        contents = [lastName, studentID, firstName, studentAge, studentAddress, studentPhoneNumber]
        file_records.writelines(str(contents) + '\n')

    file_records.close()
    print("Success. Data writen and saved to 'file_records.txt'.")
    print()


if __name__ == '__main__':
    main()
