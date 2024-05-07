class PRESENTATION:
    students_n_min: int = 0
    students_n_max: int = 0
    fin_students: list = []

    def __init__(self, students_n_min: int, students_n_max: int):
        self.students_n_min = students_n_min
        self.students_n_max = students_n_max
        pass

    def is_student_n_min(self):
        return len(self.fin_students) >= self.students_n_min

    def is_student_n_max(self):
        return len(self.fin_students) <= self.students_n_max

    def is_student_n_ok(self):
        return self.is_student_n_min() and self.is_student_n_max()


if __name__ == '__main__':
    presentation = PRESENTATION(5, 10)
    for i in range(0, 20):
        presentation.fin_students.append(i)
        print(f"{i}: {presentation.is_student_n_ok()}")
