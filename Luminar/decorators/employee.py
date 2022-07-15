class Course:
    course_name:str
    active_status:bool


    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.active_status=kwargs.get("active_status")

    def __str__(self):
        return self.course_name

class Batch:
    course:Course
    batchcode:str
    startdate:str


    def addbatch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batchcode=kwargs.get("batchcode")
        self.startdate=kwargs.get("startdate")

    def __str__(self):
        return self.batchcode



class Student:

    std_name:str
    gender:str
    rol:str
    batch:Batch

    def addstudent(self,**kwargs):
        self.std_name=kwargs.get("std_name")
        self.gender=kwargs.get("gender")
        self.rol=kwargs.get("rol")
        self.batch=kwargs.get("batch")

    def __str__(self):
        return self.std_name


#course creation

django1=Course()
django1.add_course(course_name="django",active_status=True)

bigdata1=Course()
bigdata1.add_course(course_name="big data",active_status=True)

#batch creation

batch1=Batch()
batch1.addbatch(course=django1,batchcode="djmay2k22",startdate="5-6-2022")

batch2=Batch()
batch2.addbatch(course=bigdata1,batchcode="djjune2k22",startdate="5-3-2022")

#student creation

rahul=Student()
rahul.addstudent(std_name="rahul",gender="male",rol="123",batch=batch1)

akshay=Student()
akshay.addstudent(std_name="akshay",gender="male",rol="1253",batch=batch1)

nikhil=Student()
nikhil.addstudent(std_name="nikhil",gender="male",rol="1235",batch=batch2)

poki=Student()
poki.addstudent(std_name="poki",gender="male",rol="123578",batch=batch2)

print(rahul.batch.course.course_name)
print(poki.rol)