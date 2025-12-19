# Inheritance in Python

class Person:
    # A base class to represent a person.

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        # Method to display an introduction message.
        return f"My name is {self.name}, and I'm {self.age} years old."


# Derived class: Student inherits from Person
class Student(Person):
    # A class to represent a student.

    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major

    def introduce(self):
        # Override the introduce method to include student-specific information.
        return f"My name is {self.name}, I'm {self.age} years old, and I'm studying {self.major} (ID: {self.student_id})."

    def study(self):
        return f"{self.name} is studying {self.major}."


# Derived class: Teacher inherits from Person
class Teacher(Person):
    # A class to represent a teacher.

    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    def introduce(self):
        # Override the introduce method to include teacher-specific information.
        return f"My name is {self.name}, I'm {self.age} years old, and I teach {self.subject} (Employee ID: {self.employee_id})."

    def teach(self):
        return f"{self.name} is teaching {self.subject}."


# Main function to demonstrate inheritance
def main():
    # Create a Person object
    person = Person("Alice", 40)
    print("Person:")
    print(person.introduce())

    # Create a Student object
    student = Student("Bob", 20, "S12345", "Computer Science")
    print("\nStudent:")
    print(student.introduce())
    print(student.study())

    # Create a Teacher object
    teacher = Teacher("Charlie", 35, "T98765", "Mathematics")
    print("\nTeacher:")
    print(teacher.introduce())
    print(teacher.teach())


# Entry point of the program
if __name__ == "__main__":
    main()
