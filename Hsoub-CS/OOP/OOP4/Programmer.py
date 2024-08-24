from Employee import Employee
from Roles import *
from Payments import *

class Programmer(Employee, ProgrammerRole, Salary):
    def __init__(self, first_name, last_name, salary, lang, projects = None):
        Employee.__init__(self, first_name, last_name)
        Salary.__init__(self,salary)
        ProgrammerRole.__init__(self, lang, projects)
        self.salary = salary
        self.lang = lang
        if projects is None:
            projects = []
        self.projects = projects

    def info(self):
        return f'Name: {self.first_name} {self.last_name}, Titel: {self.__class__.__name__}, Projects: {self.projects}'

    def calculate_salary(self):
        return Salary.calculate_salary(self)

    @classmethod
    def from_string(cls, string):
        first_name, last_name, salary, lang = string.split('-')
        salary = int(salary)
        return cls(first_name, last_name, salary, lang)


    def assign_project(self, project):
        self.projects.append(project)


    def get_prjects(self):
        print('Projects: ')
        print('=' * 10)
        projects_list = []
        for number , project in enumerate(self.projects):
            projects_list.append(f'{number + 1}: {project}')
        return '\n'.join(projects_list)

class FrellancerProgrammer( Employee, ProgrammerRole, Hourly_Payment):
    def __init__(self, first_name, last_name, hour_rate, work_hour, lang, projects ):
        Employee.__init__(self, first_name, last_name)
        ProgrammerRole.__init__(self, lang, projects)
        Hourly_Payment.__init__(self, work_hour, hour_rate)

    def info(self):
        return f'Name: {self.first_name} {self.last_name}, Titel: {self.__class__.__name__}, Projects: {self.projects}'

    def calculate_salary(self):
        return Hourly_Payment.calculate_salary(self)


