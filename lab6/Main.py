from lab6 import Studenci
from lab6.Studenci import StudentGrades

s = StudentGrades()
s.load_file("ocenystudenci")
s.delete_student('test2@gmail.com')
s.auto_grade()
