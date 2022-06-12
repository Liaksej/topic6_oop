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

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        sum_marks = 0
        quantity_marks = 0
        for marks_list in self.grades.values():
            for mark in marks_list:
                sum_marks += mark
            quantity_marks += len(marks_list)
        return (sum_marks / quantity_marks)

    def __str__(self):
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {self._average_grade()}\n'
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
               f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return res


    def __lt__(self, other):
        if not isinstance(other, Student):
            print('not a Student!')
            return
        return self._average_grade() < other._average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        sum_marks = 0
        quantity_marks = 0
        for marks_list in self.grades.values():
            for mark in marks_list:
                sum_marks += mark
            quantity_marks += len(marks_list)
        return (sum_marks / quantity_marks)

    def __str__(self):
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self._average_grade()}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Mentor):
            print('not a Mentor!')
            return
        return self._average_grade() < other._average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


some_student = Student('Алексей', 'Тарусов', 'мужской')
some_student.courses_in_progress += ['Python']

some_reviewer = Reviewer('Александр', 'Бардин')
some_reviewer.courses_attached += ['Python']

some_lecturer = Lecturer('Олег', 'Булыгин')
some_lecturer.courses_attached += ['Python', 'Git']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 8)
some_reviewer.rate_hw(some_student, 'Python', 10)

some_student.rate_hw(some_lecturer, 'Python', 10)
some_student.rate_hw(some_lecturer, 'Python', 10)
some_student.rate_hw(some_lecturer, 'Python', 9)


print(some_student)
print(some_student.grades)
print()
print(some_lecturer)
print(some_lecturer.grades)
print()
print(some_reviewer)