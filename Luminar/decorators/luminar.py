class Staff(object):
    id:int
    name:str
    role:str

    def __init__(self,*args,**kwargs):
        self.id=kwargs.get("id")
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")

    def __str__(self):
        return self.name

class Addcourse():
    def set_course(self,coursename,user):
        self.coursename=coursename
        self.user=user

    def __str__(self):
        return self.coursename



user=Staff(id=100,name="Rahul",role="admin")
print(user)

course=Addcourse()
course.set_course(coursename="Django",user=user)
print(course)