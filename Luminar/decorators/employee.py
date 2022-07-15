class Course:
    course_name:str
    active_status:bool


    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.active_status=kwargs.get("active_status")

    def __str__(self):
        return self.course_name
