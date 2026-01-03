class Shkolnik:
    def __init__(self, name, age, grade_level, performance, school_name):
        self.name = name
        self.age = age
        self.grade_level = grade_level
        self.performance = performance
        self.school_name = school_name
        self.grades = []
        self.lessons = []

    def go_to_school(self):
        print(f"{self.name} is going to school.")

    def go_home(self):
        print(f"{self.name} is going home.")

    def receive_grade(self, grade):
        self.grades.append(grade)

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def change_school(self, new_school):
        self.school_name = new_school