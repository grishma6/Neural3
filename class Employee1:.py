#class program
class Employee:
    employee_count = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.employee_count += 1

    def average_salary(self, *salaries):
        total_salary = sum(salaries) + self.salary
        num_employees = len(salaries) + 1
        return total_salary / num_employees


class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department, overtime_hours):
        super().__init__(name, family, salary, department)
        self.overtime_hours = overtime_hours

    def calculate_total_salary(self):
        return self.salary + (self.overtime_hours * 10)  # Assuming overtime pay is $10 per hour


# Creating instances of Employee class
employee1 = Employee("Grishma Golla", "Family1", 100000, "Software Developemnt")
employee2 = Employee("Jimmy", "Family2", 75000, "Lawyer")

# Creating instances of FulltimeEmployee class
fulltime_employee1 = FulltimeEmployee("Rosy", "Family3", 85000, "Doctor", 5)
fulltime_employee2 = FulltimeEmployee("Lilly", "Family4", 90000, "Surgeon", 8)

# Calling member functions
average_salary_all = employee1.average_salary(employee2.salary, fulltime_employee1.salary, fulltime_employee2.salary)
total_salary_fulltime_employee1 = fulltime_employee1.calculate_total_salary()
total_salary_fulltime_employee2 = fulltime_employee2.calculate_total_salary()

# Printing results
print(f"Total number of employees: {Employee.employee_count}")
print(f"Average salary of all employees: ${average_salary_all:.2f}")
print(f"Total salary for Fulltime Employee 1: ${total_salary_fulltime_employee1:.2f}")
print(f"Total salary for Fulltime Employee 2: ${total_salary_fulltime_employee2:.2f}")

#program on numpy
import numpy as np

# Create a random vector of size 20 with float values in the range 1-20
random_vector = np.random.uniform(1, 20, 20)

# Reshape the array to 4 by 5
reshaped_array = random_vector.reshape(4, 5)

# Replace the max in each row by 0 (along axis=1)
reshaped_array[np.arange(4), np.argmax(reshaped_array, axis=1)] = 0

print(reshaped_array)