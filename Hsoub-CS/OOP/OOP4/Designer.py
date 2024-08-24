from Employee import Employee
from Roles import *
from Payments import *

class Designer(Employee,DesignerRole, Salary ):
    def __init__(self, first_name, last_name, salary, apps, projects = None):
        Employee.__init__(self, first_name, last_name)
        DesignerRole.__init__(self, apps, projects)
        self.salary = salary
        self.apps = apps
        if projects is None:
            projects = []
        self.projects = projects

    def info(self):
        return f'Name: {self.first_name} {self.last_name}, Titel: {self.__class__.__name__}, Projects: {self.projects}'

    def calculate_salary(self):
        return Salary.calculate_salary(self)



class FrellancerDesigner(Employee, DesignerRole, Hourly_Payment):
    def __init__(self, first_name, last_name, hour_rate, work_hour, apps, projects ):
        Employee.__init__(self, first_name, last_name)
        DesignerRole.__init__(self, apps, projects)
        Hourly_Payment.__init__(self,hour_rate, work_hour )

    def info(self):
        return f'Name: {self.first_name} {self.last_name}, Titel: {self.__class__.__name__}, Projects: {self.projects} Work Hours: {self.work_hours}'
    def calculate_salary(self):
        return Hourly_Payment.calculate_salary(self)

