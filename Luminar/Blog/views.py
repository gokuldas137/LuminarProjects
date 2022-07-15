from Luminar.Blog.models import users, posts

session = {}


def signin_required(fn):
    def wrapper(*args, **kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("Invalid User")
    return wrapper


# username="akhil"
# password="password@123"

# for users in user:
#     if user["username"]==username and user["password"]==password:
#         print("ACCESS GRANTED")
#         break
#     else:
#         print("DENIED")

# user=[user for user in users if user["username"]==username and user["password"]==password]
# if user:
#     print("ACCESS GRANTED")
# else:
#     print("ACCESS DENIED")
def authenticate(**kwargs):
    username = kwargs.get("username")
    password = kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user


# print(authenticate(username="akhil",password="Password@123"))


# LOGIN
# get ppost put/patch delete
class LoginView:
    def post(self,*args, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        user = authenticate(username=username, password=password)  # username and pass correct aanonn check cheyan
        # print(user)
        if user:
            session["user"] = user[0]
            # key      0th value
        # print(session)


class PostListView:
    @signin_required
    def get(self,*args,**kwargs):
        return posts

class MyPostListView:
    @signin_required
    def get(self,*args,**kwargs):
        userid=session["user"]["id"]
        myposts=[post for post in posts if post["userId"]==userid]
        return myposts

login = LoginView()
login.post(username="akhil", password="Password@123")
allposts = PostListView()
print(allposts.get())


myposts=MyPostListView()
print(myposts.get())