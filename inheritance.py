#1 class defination is one time process
class ParentClass():
    #1. property/variable
    bloodgroup="b+v"
    pass
class ChildClass(ParentClass):
    pass
#2 create class external object is many time process
ceo1=ChildClass()
print(ceo1.bloodgroup)