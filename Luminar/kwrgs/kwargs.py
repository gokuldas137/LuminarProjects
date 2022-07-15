# def sum(*args):
#     return(args)
#
# print(sum(10,20,30))
# print(sum(10,20,40,50))
#
#
#
# def add(*args):
#     return sum(args)
#
# def max_fun(*args):
#     return max(args)
#
#
# def min_fun(*ar):
#     return min(ar)
# print(min(10,1,2,5,6))


#   Note:
#   *args prints values in list and **kwargs prints values in dictionary

# def add_nums(**kwargs):
#     # print(sum([v for k,v in kwargs.items()]))
#
#     add_nums(n1=10,n2=20,n3=40)
#                print(add_nums)
#

def add_nums(**kwargs):
    add_nums(n1=10, n2=20, n3=40)
    print(add_nums)