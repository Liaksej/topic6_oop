class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    pass


class Reviewer(Mentor):
    pass


some_student = Student('Алексей', 'Тарусов', 'мужской')
some_student.courses_in_progress += ['Python']

some_mentor = Mentor('Александр', 'Бардин')
some_mentor.courses_attached += ['Python']

some_mentor.rate_hw(some_student, 'Python', 10)
some_mentor.rate_hw(some_student, 'Python', 10)
some_mentor.rate_hw(some_student, 'Python', 10)

print(some_student.grades)

