class Employee():
    no_of_leaves = 8
Harry = Employee()
Rohan = Employee()
Harry.name = "Harry"
Rohan.name = "Rohan"
Harry.role = "Instructer"
Rohan.role = "Student"
Employee.no_of_leaves = 9
Rohan.no_of_leaves = 10
print(Employee.no_of_leaves)
print(Rohan.__dict__)