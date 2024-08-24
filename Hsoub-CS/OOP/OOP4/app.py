from Employee import Employee
from Manager import Manager
from Programmer import Programmer, FrellancerProgrammer
from Roles import *
from Payments import *
from Designer import *
if __name__ == '__main__':
    ahmed = Designer('Ahmed', 'ali', 5000, 'PHP', ['1', '2'])
    sara = FrellancerDesigner('Sara', 'ali', 120, 8, 'PHP', ['web', 'app'])
    print(sara.calculate_salary())
    print(sara.info())

