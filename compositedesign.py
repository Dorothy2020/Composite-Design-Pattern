from abc import ABCMeta,abstractmethod,abstractstaticmethod

class IDepartment(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,employees):
        """implement in child class"""

    @abstractstaticmethod
    def print_department():
        """implement in child class"""

class Accounting(IDepartment):
    def __init__(self,employees):
        self.employees=employees

    def print_department(self):
        print(f"Accounting Department:{self.employees}")

class Parentdepartment(IDepartment):
    def __init__(self,employees):
        self.employesss=employees
        self.base_employees=employees
        self.sub_depts=[]

    def __init__(self,dept):
        self.sub_depts.append(dept)
        self.employee +=dept.employees

    def print_department(self):
        print("Parent Department")
        print(f"Parent Department Base Employees:{self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Total number of employees:{self.employees}")

        dept1=Accounting(200)
        # dept2=Development(170)

        Parent_dept=Parentdepartment(30)
        Parent_dept.add(dept1)
        # Parent_dept.add(dept2)

        Parent_dept.print_department()


