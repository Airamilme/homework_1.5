class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lec:
                lecturer.grades_lec[course] += [grade]
            else:
                lecturer.grades_lec[course] = [grade]
        else:
            return 'Ошибка'

    def average_stu(self):
        all_grades_stu = []
        for course, grades in self.grades.items():
            if course in self.courses_in_progress:
                all_grades_stu.extend(grades)
        return sum(all_grades_stu) / len(all_grades_stu)

    def average_grade_to_course_stu(self, course):
        if course in self.courses_in_progress:
            return sum(self.grades[course]) / len(self.grades[course])
        else:
            return 'Студент не изучает курс'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Студента нет в списке')
            return
        return round((Student.average_stu(self)), 1) < round((other.average_stu()), 1)

    def __str__(self):
        result_stu = f'Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за домашние задания: {round((Student.average_stu(self)), 1)} \n Курсы в процессе изучения: {self.courses_in_progress} \n Завершенные курсы: {self.finished_courses} '
        return result_stu


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lec = {}

    def average_lec(self):
        all_grades_lec = []
        for course, grades_lec in self.grades_lec.items():
            if course in self.courses_attached:
                all_grades_lec.extend(grades_lec)
        return sum(all_grades_lec) / len(all_grades_lec)

    def average_grade_to_course_lec(self, course):
        if course in self.courses_attached:
            return sum(self.grades_lec[course]) / len(self.grades_lec[course])
        else:
            return 'Лектор не преподает на этом курсе'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Лектора нет в списке')
            return
        return round((Lecturer.average_lec(self)), 1) < round((other.average_lec()), 1)

    def __str__(self):
        result_lec = f'Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {round((Lecturer.average_lec(self)), 1)}'
        return result_lec


class Reviewer(Mentor):

    def rate_stu(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result_rev = f'Имя: {self.name} \n Фамилия: {self.surname}'
        return result_rev

def avg_all_lec(course, *args):
    grades_all_lec = []
    for lecture in args:
        if course in lecture.courses_attached:
            grades_all_lec.append(round((lecture.average_grade_to_course_lec(course)), 1))
            average_grade_lec = sum(grades_all_lec) / len(grades_all_lec)
    return f'Средняя оценка всех лекторов за курс "{course}" - {round(average_grade_lec, 1)}'

def avg_all_stu(course, *args):
    grades_all_stu = []
    for student in args:
        if course in student.courses_in_progress:
            grades_all_stu.append(round((student.average_grade_to_course_stu(course)), 1))
            average_grade_stu = sum(grades_all_stu) / len(grades_all_stu)
    return f'Средняя оценка всех студентов за домашние задания по курсу "{course}" - {round(average_grade_stu, 1)}'


first_student = Student('Timon', 'Meerkat', 'man')
first_student.courses_in_progress += ['Python', 'GIT']
first_student.finished_courses += ['Введение в программирование']

second_student = Student('Pumbaa', 'Hog', 'man')
second_student.courses_in_progress += ['Python', 'GIT']
second_student.finished_courses += ['Введение в программирование']

first_reviewer = Reviewer('Tom', 'Cat')
first_reviewer.courses_attached += ['Python', 'GIT']
second_reviewer = Reviewer('Jerry', 'Mouse')
second_reviewer.courses_attached += ['Python', 'GIT']

first_lecturer = Lecturer('Chip', 'Chipmunk')
first_lecturer.courses_attached += ['Python', 'GIT']
second_lecturer = Lecturer('Dale', 'Chipmunk')
second_lecturer.courses_attached += ['Python', 'GIT']

first_reviewer.rate_stu(first_student, 'Python', 8)
second_reviewer.rate_stu(first_student, 'Python', 6)
first_reviewer.rate_stu(first_student, 'GIT', 8)
second_reviewer.rate_stu(first_student, 'GIT', 10)
first_reviewer.rate_stu(second_student, 'Python', 10)
second_reviewer.rate_stu(second_student, 'Python', 8)
first_reviewer.rate_stu(second_student, 'GIT', 8)
second_reviewer.rate_stu(second_student, 'GIT', 8)

first_student.rate_lec(first_lecturer, 'Python', 8)
second_student.rate_lec(first_lecturer, 'Python', 10)
first_student.rate_lec(first_lecturer, 'GIT', 10)
second_student.rate_lec(first_lecturer, 'GIT', 10)
first_student.rate_lec(second_lecturer, 'Python', 5)
second_student.rate_lec(second_lecturer, 'Python', 8)
first_student.rate_lec(second_lecturer, 'GIT', 10)
second_student.rate_lec(second_lecturer, 'GIT', 6)


print(first_student)
print(first_student.grades)
print ()
print(second_student)
print(second_student.grades)
print ()
print(first_student < second_student)
print ()
print(avg_all_stu('Python', first_student, second_student))
print(avg_all_stu('GIT', first_student, second_student))
print ()
print(first_lecturer)
print(first_lecturer.grades_lec)
print ()
print(second_lecturer)
print(second_lecturer.grades_lec)
print ()
print(first_lecturer < second_lecturer)
print ()
print(avg_all_lec('Python', first_lecturer, second_lecturer))
print(avg_all_lec('GIT', first_lecturer, second_lecturer))
print ()
print(first_reviewer)
print ()
print(second_reviewer)