filename = "students3.txt"
students = {}

with open(filename, "r") as file:
    for line in file:
        data = line.strip().split(",")
        email = data[0]
        name = data[1]
        surname = data[2]
        points = int(data[3])
        if len(data) > 4:
            grade = data[4]
            student_data = [name, surname, points, grade]
            if len(data) > 5:
                status = data[5]
                student_data = [name, surname, points, grade, status]
        else:
            student_data = [name, surname, points]
        students[email] = student_data

print(students)
