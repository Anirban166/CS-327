# creating a class named "Employee":
class Employee:
   'Common base class for all employees'
   # counter variable to hold count of Employee objects
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1 # increment counter variable
   
   # creating a function to display object count:
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)
   
   # creating a function to display the attributes name and salary:
   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

# creating two Employee objects:
"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
# displaying them via Employee::displayEmployee() function:
emp1.displayEmployee()
emp2.displayEmployee()
# displaying total Employee object count:
print ("Total Employee %d" % Employee.empCount)
