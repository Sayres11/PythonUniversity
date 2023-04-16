import smtplib
from email.mime.text import MIMEText

students = {}


def load_file(file):
    with open(file, "r") as file:
        for line in file:
            data = line.strip().split(",")
            email = data[0]
            name = data[1]
            surname = data[2]
            points = int(data[3])
            grade = data[4] if len(data) > 4 and not "None" else None
            status = data[5] if len(data) > 5 and not "None" else None
            student_data = {"name": name, "surname": surname, "points": points, "grade": grade, "status": status}
            students[email] = student_data
    print(students)


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()

    # subject = "Email wysłany z Python'a"
    # body = "To jest wiadomość wysłana za pomocą SMTP"
    # sender = "test@gmail.com"
    # recipients = ["test2@gmail.com"]
    # password = "haslo app gmaila"
    # send_email(subject, body, sender, recipients, password)


def auto_grade():
    for email, data in students.items():
        if data['grade'] is None or "None":
            points = data["points"]
            if points >= 91:
                grade = 5
            elif points >= 81:
                grade = 4.5
            elif points >= 75:
                grade = 4
            elif points >= 70:
                grade = 3.5
            elif points >= 60:
                grade = 3
            elif points >= 50:
                grade = 2
            data["grade"] = grade
            data["status"] = "GRADED"
    save_file()


def add_student(email, name, surname, points, grade=None, status=None):
    if email in students:
        print("Podany adres e-mail jest już zajęty")
        return
    student_data = {"name": name, "surname": surname, "points": points, "grade": grade, "status": status}
    students[email] = student_data
    save_file()


def delete_student(email):
    if email in students:
        del students[email]
        print(f"Student {email} został usunięty")
    else:
        print(f"Student {email} nie został znaleziony")
    save_file()

def save_file():
    filepath = "studentsOut.txt"
    with open(filepath, "w") as file_object:
        for email, student_data in students.items():
            name = student_data["name"]
            surname = student_data["surname"]
            points = student_data["points"]
            grade = student_data["grade"]
            status = student_data["status"]
            file_object.write(f"{email},{name},{surname},{points},{grade},{status}\n")
            print("File saved")


load_file("studentsOut.txt")
auto_grade()
save_file()
