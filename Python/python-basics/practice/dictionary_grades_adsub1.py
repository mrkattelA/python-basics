def ave(x):
    average = sum(x)/len(x)
    return average

def main():
    grades = {}

    grades["English"] = int(input("Enter the Grade of English: "))
    grades["Math"] = int(input("Enter the Grades of Math: "))
    grades["Global Studies"] = int(input("Enter the Grades of Global Studies: "))
    grades["Art"] = int(input("Enter the Grades of Art: "))
    grades["Music"] = int(input("Enter the Grades of Math: "))

    gradespoints = grades.values()

    averages = ave(gradespoints)

    print(f'The average grade is {averages}.')

    print("Please change the grade of one subject and get new average: ")
    select_subject = input("Please Enter the Subject: ")
    select_grade = input("Please enter the value of " + select_subject + "is :")

    grades[select_subject] = int(select_grade)

    averages = ave(gradespoints)

    print(f'The new average grade is {averages}.')

main()