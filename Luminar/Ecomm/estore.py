# get - retrieve
# post - create
# put/patch - update
# delete - remove/delete


class User:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.role = kwargs.get("role")


class AddProduct:
    def post(self, **kwargs):
        user = kwargs.get("user")
        if user.role == "admin":
            self.product_name = kwargs.get("product_name")
            self.user = kwargs.get("user")
        else:
            print("No Access")


us_er = User(name="rahul", role="hr")
pro1 = AddProduct()
pro1.post(p_name="Laptop", user=us_er)
