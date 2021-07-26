class Student:
    university = 'Mumbai University'
    count = 0
    def __init__(self):
        self.status = 'Active'
        self.id = ''
        self.name = ''
        Student.count += 1
    def tp(self,new_status,assig_id,assig_name):
        self.status = new_status
        self.id = assig_id
        self.name = assig_name
        if self.status == 'Suspend':
            Student.count -= 1
       # elif self.status in ['Suspend'] and new_status =='Active':
        #    Student.count += 1



studnet_1 = Student()
studnet_2 = Student()
studnet_3 = Student()

studnet_1.tp('Suspend','1','abc')
studnet_2.tp('Active','2','xyz')
studnet_1.tp('Active','3','pqr')

print(studnet_1.status,studnet_1.name,studnet_1.id)
print(studnet_2.status,studnet_2.name,studnet_2.id)
print(studnet_3.status,studnet_3.name,studnet_3.id)
print(Student.count)




