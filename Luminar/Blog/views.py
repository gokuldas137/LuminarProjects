from Luminar.Blog.models import users

username="akhil"
password="password@123"

# for users in user:
#     if user["username"]==username and user["password"]==password:
#         print("ACCESS GRANTED")
#         break
#     else:
#         print("DENIED")

user=[user for user in users if user["username"]==username and user["password"]==password]
if user:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
