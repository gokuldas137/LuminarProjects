from Luminar.Authentication.models import users

def authenticate(**kwargs):
    uname=kwargs.get("username")
    pasw=kwargs.get("password")
    user=[user for user in users if user["username"]==uname and user["password"]==pasw]
    print(user)



authenticate(username="django",password="django@123")