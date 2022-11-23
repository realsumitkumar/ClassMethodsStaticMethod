class Employee:
    no_of_leaves = 8

    def __init__(self, aname, arole, asalary):
        self.name = aname
        self.role = arole
        self.salary = asalary

    def print_details(self):
        print(f"name is {self.name} with role as {self.role} and salary is {self.salary}")

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def just_string(string):
        print("this is good " + string)


sumit = Employee("sumit", "programmer", 12000)
rohan = Employee.from_dash("rohan-teacher-4600")

rohan.just_string("sumit")
