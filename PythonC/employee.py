class employee:
    Company_Name = 'TryCatch'
    count = 0
    def __init__(self):
        self.id = ''
        self.name = ''
        self.salary = ''
        employee.count += 1

    def compute(self,n_id,n_name,n_salary):
        self.id = n_id
        self.name = n_name
        self.salary = int(n_salary)
        self.salary = self.salary*1.15


emp1 = employee()
emp2 = employee()

emp1.compute('1','abc',15000)
emp2.compute('2','pqr',20000)

print(emp1.id,emp1.name,emp1.salary)
print(emp2.id,emp2.name,emp2.salary)

print("Total employees" , employee.count)
