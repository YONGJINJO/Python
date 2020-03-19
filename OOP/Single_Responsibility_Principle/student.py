class Student:
    def __init__(self, name, id, major):
        self.student_info = Student_Info(name, id, major)
        self.grades = Grade()

    def print_report_card(self):
        return "코드잇 대학\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}\n".format(self.student_info.name, self.student_info.id, self.student_info.major, self.grades.get_average_grades())

class Student_Info:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major

    def change_student_info(self, new_name, new_id, new_major):
        '''학생 인적사항으로 수정 메소드'''
        self.name = new_name
        self.id = new_id
        self.major = new_major

class Grade:
    def __init__(self):
        self.grades = []

    def add_grade(self, value):
        """학점 추가 메소드"""
        self.grades.append(value) if 0 <= value <= 4.3 else print("수업 학점은 0과 4.3 사이여야 합니다.")

    def get_average_grades(self):
        return sum(self.grades) / len(self.grades)


student = Student("강영훈", 20130024, "통계학과")
student.student_info.change_student_info("강영훈", 20130024, "컴퓨터 공학과")
student.grades.add_grade(3.0)
student.grades.add_grade(3.33)
student.grades.add_grade(3.67)
student.grades.add_grade(4.3)

print(student.print_report_card())