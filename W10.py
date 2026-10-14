class Person:
    def __init__(self, name, address, weight, height):
        self.name = name
        self.address = address
        self.weight = weight
        self.height = height
        self.bmi = self.getBMI()
        
    def show(self):
        print(f"Name: {self.name}, Address: {self.address}, Weight: {self.weight}, Height: {self.height}")
        print(f"BMI: {self.bmi}")
        
    def getBMI(self):
        self.bmi = self.weight / (self.height ** 2)
        return self.bmi
    
# p1 = Person("Peem", "213 Pakkhlong", 120, 1.60)
# p1.show()

class Student(Person):
    def __init__(self, name, address, weight, height, student_id, course, gpa):
        super().__init__(name, address, weight, height)
        self.student_id = student_id
        self.course = course
        self.gpa = gpa
    def show(self):
        super().show()
        print(f"Student ID: {self.student_id}, Course: {self.course}, GPA: {self.gpa}")
    
p1 = Student("Peem", "213 Pakkhlong", 120, 1.60, 6901012610391, "Computer Engineering", 2.5)
p1.show()

class Employee(Person):
    def __init__(self, name, address, weight, height, employee_id, department, salary):
        super().__init__(name, address, weight, height)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
    def show(self):
        super().show()
        print(f"Employee ID: {self.employee_id}, Department: {self.department}, Salary: {self.salary}")
    
# p1 = Employee("Peem", "213 Pakkhlong", 120, 1.60, 27147, "CEO", 350000)
# p1.show()