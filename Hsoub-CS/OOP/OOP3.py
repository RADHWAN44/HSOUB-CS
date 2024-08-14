import datetime
from abc import ABC, abstractmethod

class Employee(ABC):
    total = 0
    salary_raice = 1.1

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        Employee.total += 1
    @abstractmethod
    def info(self):
        pass
    @abstractmethod
    def calculate_salary(self):
        pass

    @classmethod
    @abstractmethod
    def from_string(cls, string):
        first_name, last_name, title, salary = string.split('_')
        salary = int(salary)
        return cls(first_name, last_name, title)

    @staticmethod
    def iss_workday(day):
        if day.weekday() == 4 or day.weekday() == 5:
            return False
        return True






class Manager(Employee):
    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name)
        self.salary = salary
        if employees is None:
            employees = []
        self.employees = employees

    def info(self):
        return f'Name:{self.first_name} {self.last_name}, Titel: {self.__class__.__name__} '

    def calculate_salary(self):
        return self.salary
    @classmethod
    def from_string(cls, string):
        first_name, last_name, salary = string.split('_')
        salary = int(salary)
        return cls(first_name, last_name, salary)

    def get_employees(self):
        print('Employees: ')
        print('=' * 10)
        employees_list = []
        for number , employee in enumerate(self.employees):
            employees_list.append(f'{number + 1}: {employee.info()}')
        return '\n'.join(employees_list)



class Programer(Employee):
    def __init__(self, first_name, last_name, salary, lang, projects = None):
        super().__init__(first_name, last_name)
        self.salary = salary
        self.lang = lang
        if projects is None:
            projects = []
        self.projects = projects

    def info(self):
        return f'Name: {self.first_name} {self.last_name}, Titel: {self.__class__.__name__}, Projects: {self.projects}'

    def calculate_salary(self):
        return self.salary

    @classmethod
    def from_string(cls, string):
        first_name, last_name, salary, lang = string.split('-')
        salary = int(salary)
        return cls(first_name, last_name, salary, lang)


    def assign_project(self, project):
        self.projects.append(project)



class Accoutant(Employee):
    def __init__(self, first_name, last_name, salary, projects = None):
        super().__init__(first_name, last_name)
        self.salary = salary
        if projects is None:
            projects = []
        self.projects = projects

    def info(self):
        return f'Name: {self.first_name} {self.last_name}, Titel: {self.__class__.__name__}, Projects: {self.projects}'

    def calculate_salary(self):
        return self.salary

    def from_string(cls, string):
        first_name, last_name, salary = string.split('=-')
        salary = int(salary)
        return cls(first_name, last_name, salary)

    def get_progects(self):
        print('Projects:')
        print('=' * 10)
        projects = []
        for number , project in enumerate(self.projects):
            projects.append(f'{number + 1}: {project}')
        return '\n'.join(projects)

    def assign_project(self, project):
        self.projects.append(project)




ali = Accoutant('Ali', ' noor', 8000)
ali.assign_project(['P1', 'P2'])
print(ali.get_progects())





























