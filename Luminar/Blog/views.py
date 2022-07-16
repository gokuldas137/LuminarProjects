from Luminar.Blog.models import users, posts

# post - post
# get - retrieve                      # videos 29 and 30
# put/patch - update
# delete - delete


# authenticate

session = {}


# us_er=[user for user in users if user["username"]==username and user["password"]==password ]
# print(us_er)

def signin_required(fn):
    def wrapper(*args, **kwargs):
        if "user" in session:
            return fn(*args, **kwargs)
        else:
            print("invalid session you must login")

    return wrapper


def authenticate(*args, **kwargs):
    username = kwargs.get("username")
    password = kwargs.get("password")
    us_er = [user for user in users if user["username"] == username and user["password"] == password]
    return us_er


# print(authenticate(username="akhil", password="Password@123"))

# print(authenticate(username="vinu",password="Password@123"))

class LoginView:
    def post(self, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        user = authenticate(username=username, password=password)
        if user:
            session["user"] = user[0]
        # print(session)


class PostListView:
    @signin_required
    def get(self, **kwargs):
        return posts

    @signin_required
    def post(self, *args, **kwargs):
        userId = session["user"]["id"]
        # print(kwargs)
        post = kwargs.get("data")
        post["userId"] = userId
        print(post)
        posts.append(post)
        print("posted successfully")
        print(posts[0])


class MyPostListView:
    @signin_required
    def get(self, *args, **kwargs):
        userId = session["user"]["id"]
        my_post = [post for post in posts if post["userId"] == userId]
        return my_post


class AddLike:
    @signin_required
    def post(self, *args, **kwargs):
        postid = kwargs.get("postid")
        post = [post for post in posts if post["postId"] == postid]
        if post:
            post = post[0]
            userid = session["user"]["id"]
            post["liked_by"].append(userid)
            print(post["liked_by"])


log_in = LoginView()
log_in.post(username="richard", password="Password@123")
all_post = PostListView()
# print(all_post.get())
# print(session)
# mypostlistview=MyPostListView()
# print(mypostlistview.get())
my_post = {
    "postId": 9, "title": "hello goodmorning", "content": "mycontent", "liked_by": []
}
all_post.post(data=my_post)

like = AddLike()
like.post(postid=1)
