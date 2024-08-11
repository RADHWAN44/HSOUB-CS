import datetime


class Employee:
    total = 0
    salary_raice = 1.1

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.__salary = salary
        Employee.total += 1

    def info(self):
        return f'Name: {self.first_name} {self.last_name} '

    def set_salary(self, salary):
        if salary < 0:
            raise ValueError
        self.__salary  = salary
    def get_salary(self):
        return self.__salary



    @classmethod
    def change_raice(cls, amount):
        cls.salary_raice = amount

    @classmethod
    def from_string(cls, string):
        first_name, last_name, title, salary = string.split('_')
        salary = int(salary)
        return cls(first_name, last_name, title, salary)

    @staticmethod
    def iss_workday(day):
        if day.weekday() == 4 or day.weekday() == 5:
            return False
        return True






class Manager(Employee):
    def __init__(self, first_name, last_name, salary, employees):
        super().__init__(first_name, last_name, salary)
        self.employees = employees
    def get_employees(self):
        print('Employees: ')
        print('=' * 10)
        employees_list = []
        for number , employee in enumerate(self.employees):
            employees_list.append(f'{number + 1}: {employee.info()}')
        return '\n'.join(employees_list)



class Accoutant(Employee):
    pass

class Programer(Employee):
    def __init__(self,first_name,last_name, salary, lang, projects):
        super().__init__(first_name, last_name, salary)
        self.lang = lang
        self.projects = projects

    def display_projects(self):
        print('\nProjects: ')
        print('=' * 10)
        projects_list = []
        for number , employee in enumerate(self.projects):
            projects_list.append(f'{number + 1}: {employee}')
        return '\n'.join(projects_list)


class Project:
    def __init__(self, name, description, days, done):
        self.name = name
        self.description = description
        self.days = days
        self.done = done
    def get_project(self):
        return f'Project name: {self.name}, Description: {self.description}, Days: {self.days}, Done: {self.done}'


mazen = Programer('mazen', 'noor', 5000, ['C++', 'C#', 'PHP'], ['P1', 'P2', 'P3'] )
ali = Programer('ali', 'kamal', 4000, ['Python', 'Java'], ['P1', 'P2'])
jasmin = Programer('jasmin', 'hasan', 4500, ['JavaScribt'], ['P1'])

project_1 = Project('P1', 'Estates', '2024-12-31', False)
project_2 = Project('P2', 'Stock', '2023-12-31', True)
project_3 = Project('P3', 'Hotels', '2025-10-1', False )

print(mazen.display_projects())
print(ali.display_projects())


print(project_3.get_project())
print(project_1.get_project())




























