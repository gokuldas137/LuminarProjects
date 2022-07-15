def admin_only(fn):
    def wrapper(**kwargs):
        user=kwargs.get("user")
        if user.role != "admin":
            print("admin permission required")
        else:
            fn(kwargs)
    return wrapper


class Employee():

    def __init__(self, **kwargs):  # eid = employee id
        self.eid = kwargs.get("eid")
        self.name = kwargs.get("name")
        self.role = kwargs.get("role")

    def __str__(self):
        return self.name


# employee=Employee(1234,"rahul","hr")
# print(employee)


class Department():


    @admin_only
    def __init__(self, **kwargs):
        user = kwargs.get("user")
        if user.role == "admin":
            self.dept_name = kwargs.get("dept_name")
            self.user = kwargs.get("user")
        else:
            print("no access")

    def __str__(self):
        return self.dept_name


employee = Employee(name="rahul", role="hr")
# print(employee)
department = Department(dept_name="finance", user=employee)
print(department)
