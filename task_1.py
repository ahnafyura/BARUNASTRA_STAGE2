import abc
from abc import ABC, abstractmethod

class employee(ABC):
    def __init__(self, EmployeeName, EmployeeID):
        self._EmployeeName = EmployeeName
        self._EmployeeID = EmployeeID
    
    @property
    def EmployeeName(self):
        return self._EmployeeName
    
    @property
    def EmployeeID(self):
        return self._EmployeeID
    
    @abstractmethod
    def calculateWeeklyPay(self):
        pass
    
class sallaried(employee):
    def __init__ (self, EmployeeName, EmployeeID, EmployeeSalary):
        super().__init__(EmployeeName, EmployeeID)
        self._EmployeeSalary = EmployeeSalary
    
    def calculateWeeklyPay(self):
        return self._EmployeeSalary / 52

class Hourly(employee):
    def __init__ (self, EmployeeName, EmployeeID, HourWoeked, HourlyRate):
        super().__init__(EmployeeName, EmployeeID)
        self._HourWoeked = HourWoeked
        self._HourlyRate = HourlyRate
    
    def calculateWeeklyPay(self):
        return self._HourWoeked * self._HourlyRate
    
class PayrollSystem:
    def __init__ (self):
        self._employeeHere = []
    
    def addEmployee(self, employee):
        self._employeeHere.append(employee)

    def calculatePayroll(self):
        pembatas = f"+{'-'*27}+{'-'*12}+{'-'*16}+"
        
        print("\nPAYROLL REPORT")
        print(pembatas)
        print(f"| {'Employee Name':<25} | {'ID':<10} | {'Weekly Pay':>14} |")
        print(pembatas)

        totalPayroll = 0.0

        for ListEmployee in self._employeeHere:
            if isinstance(ListEmployee, sallaried):
                pay = ListEmployee.calculateWeeklyPay()
                print(f"| {ListEmployee.EmployeeName:<25} | {ListEmployee._EmployeeID:<10} | ${pay:>13.2f} |")
                totalPayroll += pay
            
        for ListEmployee in self._employeeHere:
            if isinstance(ListEmployee, Hourly):
                pay = ListEmployee.calculateWeeklyPay()
                print(f"| {ListEmployee.EmployeeName:<25} | {ListEmployee._EmployeeID:<10} | ${pay:>13.2f} |")
                totalPayroll += pay

        print(pembatas)
        print(f"| {'TOTAL PAYROLL':<38} | ${totalPayroll:>13.2f} |")
        print(pembatas)
        print(" ")

if __name__ == "__main__":
    payrollSystem = PayrollSystem()

    try:
        n = int(input())
    except ValueError:
        print("Inputnya harus angka gng")
        exit()

    for _ in range(n):
        dataInput = input().split()

        tipeData = dataInput[0]
        namaEmployee = dataInput[1]
        tipeID = dataInput[2]

        if tipeData.lower() in ["salaried", "s"]:
            Salary = float(dataInput[3])
            employeeSallaried = sallaried(namaEmployee, tipeID, Salary)
            payrollSystem.addEmployee(employeeSallaried)
            
        elif tipeData.lower() in ["hourly", "h"]:
            TypeHourlyRate = float(dataInput[3])   
            TypeHourWorked = float(dataInput[4])
            employeeHourly = Hourly(namaEmployee, tipeID, TypeHourWorked, TypeHourlyRate)
            payrollSystem.addEmployee(employeeHourly)
    
    payrollSystem.calculatePayroll()