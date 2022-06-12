class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

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


# Экземпляры студентов
student1 = Student('Алексей', 'Тарусов', 'мужской')
student2 = Student('Анастасия', 'Банщикова', 'женский')
student1.courses_in_progress += ['Python', 'Git']
student2.courses_in_progress += ['Python']
student1.finished_courses += ['Введение в программирование']
student2.finished_courses += ['Введение в программирование']

#Экземпляры экспертов
reviewer1 = Reviewer('Олег', 'Булыгин')
reviewer2 = Reviewer('Александр', 'Бардин')
reviewer1.courses_attached += ['Python', 'Git']
reviewer2.courses_attached += ['Python', 'Git']

# Экземпляры лекторов
lecturer1 = Lecturer('Олег', 'Булыгин')
lecturer2 = Lecturer('Елена', 'Никитина')
lecturer1.courses_attached += ['Python', 'Git']
lecturer2.courses_attached += ['Python', 'Git']

# Оценки первого студента
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Git', 10)
reviewer1.rate_hw(student1, 'Python', 4)

# Оценки второго студента
reviewer2.rate_hw(student2, 'Python', 3)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 4)

# Оценки первого лектора
student1.rate_hw(lecturer1, 'Git', 10)
student1.rate_hw(lecturer1, 'Git', 10)
student1.rate_hw(lecturer1, 'Python', 6)
student2.rate_hw(lecturer1, 'Python', 10)
student2.rate_hw(lecturer1, 'Python', 10)
student2.rate_hw(lecturer1, 'Python', 6)

#Оценки второго лектора
student1.rate_hw(lecturer2, 'Python', 4)
student1.rate_hw(lecturer2, 'Python', 5)
student1.rate_hw(lecturer2, 'Python', 6)
student2.rate_hw(lecturer2, 'Python', 5)
student2.rate_hw(lecturer2, 'Python', 5)
student2.rate_hw(lecturer2, 'Python', 6)

#Списки студентов и лекторов
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]


def average_mark(persons_list, course):
    '''Функция, рассчитывающая среднюю оценку за курс

    Фукнцию можно вызывать для любого курса как студентов, так и лекторов'''
    quantity_persons = len(persons_list)
    average_value = 0
    for person in persons_list:
        sum_marks = 0
        qantity_marks = 0
        for course_name, marks_list in person.grades.items():
            if course_name == course:
                for mark in marks_list:
                   sum_marks += mark
                qantity_marks += len(marks_list)
        if qantity_marks != 0:
            average_value += (sum_marks / qantity_marks)
    return (average_value / quantity_persons)


print(student1)
print(student1.grades)
print()
print(student2)
print(student2.grades)
print()
print()

print(lecturer1)
print(lecturer1.grades)
print()
print(lecturer2)
print(lecturer2.grades)
print()
print()

print(reviewer1)
print()
print(reviewer2)
print()
print()

print(f'Лектор {lecturer1.name} {lecturer1.surname} круче, чем {lecturer2.name} {lecturer2.surname}?',
      'Ответ:', lecturer1 > lecturer2)
print()
print()

print(f'Средняя оценка за домашние задания по всем '
      f'студентам в рамках конкретного курса: {average_mark(students_list, "Python")}')
print(f'Cредняя оценки за лекции всех лекторов в рамках курса: {average_mark(lecturers_list, "Git")}')
