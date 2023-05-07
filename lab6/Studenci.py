import smtplib
from email.mime.text import MIMEText

from lab6.MyLinkedList import Lista


class Student:
    def __init__(self, email, name, surname, points, grade=None, status=None):
        self.email = email
        self.name = name
        self.surname = surname
        self.points = points
        self.grade = grade
        self.status = status

    def to_dict(self):
        return {"email": self.email, "name": self.name, "surname": self.surname, "points": self.points,
                "grade": self.grade,
                "status": self.status}


class StudentGrades:
    def __init__(self):
        self.students = Lista()

    def load_file(self, file):
        with open(file, "r") as f:
            for line in f:
                data = line.strip().split(",")
                email, name, surname = data[0:3]
                points = [int(x) for x in data[3:16]]
                grade = data[17] if len(data) >= 18 and data[12] != "None" else None
                status = data[18] if len(data) >= 14 and data[13] != "None" else None
                student_data = {'email': email, 'name': name, 'surname': surname, 'points': points, 'grade': grade,
                                'status': status}
                self.students.add(student_data)
        print(self.students)

    def send_email(self, subject, sender, password):
        for email, data in self.students.items():
            name = data["name"]
            grade = data["grade"]
            status = data["status"]
            if grade is not None and status != "MAILED":
                body = f"{name}, twoja ocena {grade}. Pozdrawiam!"
                msg = MIMEText(body)
                msg['Subject'] = subject
                msg['From'] = sender
                msg['To'] = email
                smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                smtp_server.login(sender, password)
                smtp_server.sendmail(sender, email, msg.as_string())
                smtp_server.quit()
                print(f"Email sended")
                data["status"] = "MAILED"
            else:
                print(f"{email} nie ma oceny")
        self.save_file()

    def auto_grade(self):
        for data in self.students:
            if data['grade'] is None or data['grade'] == "None" and data['status'] not in ["MAILED", "GRADED"]:
                points = data["points"]
        self.save_file()

    def add_student(self, email, name, surname, points, grade=None, status=None):
        if email in self.students:
            print("Podany adres e-mail jest już zajęty")
            return
        student_data = {"email": email, "name": name, "surname": surname, "points": points, "grade": grade,
                        "status": status}
        self.students.add(student_data)
        self.save_file()

    def delete_student(self, email):
        deleted = self.students.delete(email)
        if deleted:
            print(f"Student {email} został usunięty")
            self.save_file()
        else:
            print(f"Student {email} nie został znaleziony")

    def save_file(self):
        filepath = "studentsOut.txt"
        with open(filepath, "w") as file_object:
            for student_data in self.students:
                email = student_data["email"]
                name = student_data["name"]
                surname = student_data["surname"]
                points = student_data["points"]
                grade = student_data["grade"]
                status = student_data["status"]
                file_object.write(f"{email},{name},{surname},{points},{grade},{status}\n")
        print("File saved")
