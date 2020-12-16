class Employee(object):
    next_employee_number = 0

    def __init__(self, name, hours_worked=0.00, hourly_rate=9.25):
        self.name = name
        self.number = Employee.next_employee_number
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        Employee.next_employee_number += 1

    def add_hours(self, h):
        self.hours_worked += h

    def __str__(self):
        l = []
        l.append("Name: {:s}".format(self.name))
        l.append("ID: {:d}".format(self.number))
        l.append("Hours: {:.2f}".format(self.hours_worked))
        l.append("Rate: {:.2f}".format(self.hourly_rate))
        l.append("Wages: {:.2f}".format(self.hourly_rate * self.hours_worked))
        return "\n".join(l)
