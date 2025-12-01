import abc
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, emp_id):
        self._name = name
        self._id = emp_id
    
    @property
    def name(self):
        return self._name
    
    @property
    def emp_id(self):
        return self._id
    
    @abstractmethod
    def calculate_weekly_pay(self):
        pass

class Salaried(Employee):
    def __init__(self, name, emp_id, annual_salary):
        super().__init__(name, emp_id)
        self._annual_salary = annual_salary
    
    def calculate_weekly_pay(self):
        return self._annual_salary / 52

class Hourly(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self._hourly_rate = hourly_rate
        self._hours_worked = hours_worked
    
    def calculate_weekly_pay(self):
        return self._hours_worked * self._hourly_rate
    
class PayrollSystem:
    def __init__(self):
        self._employee_list = []
    
    def add_employee(self, employee):
        self._employee_list.append(employee)

    def calculate_payroll(self):
        pembatas = f"+{'-'*27}+{'-'*12}+{'-'*16}+"
        print("\nPAYROLL REPORT")
        print(pembatas)
        print(f"| {'Employee Name':<25} | {'ID':<10} | {'Weekly Pay':>14} |")
        print(pembatas)

        total_payroll = 0.0

        for emp in self._employee_list:
            if isinstance(emp, Salaried):
                pay = emp.calculate_weekly_pay()
                print(f"| {emp.name:<25} | {emp.emp_id:<10} | ${pay:>13.2f} |")
                total_payroll += pay
            
        for emp in self._employee_list:
            if isinstance(emp, Hourly):
                pay = emp.calculate_weekly_pay()
                print(f"| {emp.name:<25} | {emp.emp_id:<10} | ${pay:>13.2f} |")
                total_payroll += pay

        print(pembatas)
        print(f"| {'TOTAL PAYROLL':<38} | ${total_payroll:>13.2f} |")
        print(pembatas)
        print(" ")

if __name__ == "__main__":
    system = PayrollSystem()
    try:
        raw_n = input()
        if not raw_n:
            print("Yaampun Input kosong")
            exit()
        n = int(raw_n)
    except ValueError:
        print("Input jumlah harus angka gng")
        exit()

    for _ in range(n):
        raw_input = input().split()
        type_emp = raw_input[0]
        name = raw_input[1]
        emp_id = raw_input[2]

        if type_emp.lower() in ["salaried", "s"]:
            salary = float(raw_input[3])
            emp = Salaried(name, emp_id, salary)
            system.add_employee(emp)
            
        elif type_emp.lower() in ["hourly", "h"]:
            rate = float(raw_input[3])
            hours = float(raw_input[4])
            emp = Hourly(name, emp_id, rate, hours)
            system.add_employee(emp)

    system.calculate_payroll()
