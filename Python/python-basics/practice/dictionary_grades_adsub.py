def main ():
    grades = {
        "English" : 0,
        "Math" : 0,
        "Global Studies" : 0,
        "Art" : 0,
        "Music" : 0
    }

    grades["English"] = int(input("Enter the Grade of English: "))
    grades["Math"] = int(input("Enter the Grades of Math: "))
    grades["Global Studies"] = int(input("Enter the Grades of Global Studies: "))
    grades["Art"] = int(input("Enter the Grades of Art: "))
    grades["Music"] = int(input("Enter the Grades of Math: "))

    a,b,c,d,e = grades.values()

    total = a+b+c+d+e
    average = total/5

    print(f'English grade is {a}.')
    print(f'Math grade is {b}.')
    print(f'Global Studies grade is {c}.')
    print(f'Art grade is {d}.')
    print(f'Music grade is {e}.')
    print(f'The average grade is {average}.')

    print("Please change the grade of one subject and get new average: ")
    select_subject = str(input("Please Enter the Subject: "))
    select_grade = int(input("Enter the grade: "))
    grades[select_subject] = select_grade

    a,b,c,d,e = grades.values()

    total = a+b+c+d+e
    average = total/5

    print(f'The average grade is {average}.')

main()