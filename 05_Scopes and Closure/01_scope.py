username = "Bhumi"

# {} : scopes

def test():
    # username = "chai"
    print(username)

print(username) #Bhumi
test()


x = 99 #=>global
# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)



# def fun3():
#     global x 
#     x = 12

# fun3()
print(x) 



def f1():
    x = 88
    def f2():
        print(x) #->88
    return f2()  #refernece og f2 yaa whir uska definition bhej rahe h
my_res = f1()


def chaiCoder(num):
    def actual(x):
        return x**num
    return actual

f = chaiCoder(2)
g = chaiCoder(3)
print(f(3))
print(g(3))