def display(*args):
    print("data types ",type(args))
    print(args)

display(1,2,3)

display(1,2,3,4,5,6)


def add(*params):
    print(params)
    for p in params:
        print(p)

add(1,2)
add(100,101,399)

def info(**kwargs):
    print("data type of kwargs",type(kwargs))
    print(kwargs)
    print("name ",kwargs["name"])

info(name="raghu",city="Bengaluru")

#fname = "Tobias", lname = "Refsnes"


def enroll(name,email,aadhar=None):
    print("name = ",name, " email = ",email, " aadhar =",aadhar)

enroll("raghu","prasadraghuks@gmail.com")

enroll("rakesh","rakesh@gmail.com",123444)

#__init__ constructure

"""
multiple constructors

python - only one constructor __init__

you can pass some parameter which is not mandatory as None
"""

def test():
    pass
print(test)


def testargs(*args,**kwargs):
    print("args :", args)
    print("kwargs ",kwargs)
testargs(2,3,4,name="raghu")


