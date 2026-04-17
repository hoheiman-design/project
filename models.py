from abc import ABC, abstractmethod

# 1. Abstraction
class Person(ABC):
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number


    @abstractmethod
    def generate_report(self):
        pass

# 2. Inheritance
class Student(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        # 3. Encapsulation 
        self.__grades = {} 
        self.conduct_score = "B" 

    # Setter
    def add_grade(self, subject, score):
        if 0 <= score <= 100:
            self.__grades[subject] = score
        else:
            print(f"Error: Invalid score {score} for {subject}")

    def get_average(self):
        if not self.__grades: return 0
        return sum(self.__grades.values()) / len(self.__grades)

    # 
    def generate_report(self):
        avg = self.get_average()
        return f"[STUDENT REPORT] Name: {self.name} | Avg Score: {avg:.1f} | Conduct: {self.conduct_score}"

# 2. Inheritance
class Teacher(Person):
    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department

    def generate_report(self):
        return f"[TEACHER INFO] Name: {self.name} | Department: {self.department}"