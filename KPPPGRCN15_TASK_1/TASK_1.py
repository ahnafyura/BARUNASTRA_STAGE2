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

class SalariedEmployee(Employee):
    def __init__(self, name, emp_id, annual_salary):
        super().__init__(name, emp_id)
        self._annual_salary = annual_salary
    
    def calculate_weekly_pay(self):
        return self._annual_salary / 52

class HourlyEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self._hourly_rate = hourly_rate
        self._hours_worked = hours_worked
    
    def calculate_weekly_pay(self):
        return self._hours_worked * self._hourly_rate
    
class PayrollSystem:
    def __init__(self):
        self._listEmployees = []
    
    def add_employee(self, employee):
        self._listEmployees.append(employee)
    
    def run_payroll(self):
        total_payroll = 0.0
        
        for emp in self._listEmployees:
            if isinstance(emp, SalariedEmployee):
                pay = emp.calculate_weekly_pay()
                print(f"{emp.name} (ID: {emp.emp_id}): ${pay:.2f}")
                total_payroll += pay
            
        for emp in self._listEmployees:
            if isinstance(emp, HourlyEmployee):
                pay = emp.calculate_weekly_pay()
                print(f"{emp.name} (ID: {emp.emp_id}): ${pay:.2f}")
                total_payroll += pay                
        print("") 
        print(f"Total payroll: ${total_payroll:.2f}")

if __name__ == "__main__":
    system = PayrollSystem()
    try:
        raw_n = input()
        if not raw_n:
            exit()
        n = int(raw_n)
    except ValueError:
        exit()

    for _ in range(n):
        try:
            raw_input = input().split()
            if not raw_input: continue

            type_emp = raw_input[0]
            name = raw_input[1]
            emp_id = raw_input[2]

            if type_emp.lower() in ["salaried", "s"]:
                salary = float(raw_input[3])
                emp = SalariedEmployee(name, emp_id, salary)
                system.add_employee(emp)
                
            elif type_emp.lower() in ["hourly", "h"]:
                rate = float(raw_input[3])
                hours = float(raw_input[4])
                emp = HourlyEmployee(name, emp_id, rate, hours)
                system.add_employee(emp)
        except IndexError:
            continue

    system.run_payroll()