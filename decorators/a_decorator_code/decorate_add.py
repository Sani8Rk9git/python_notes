def greet(fnx):
    def mfnx(*args):
        print("This is adding tool")
        fnx(*args)
        print("Thanks for using")

    return mfnx

@greet
def add(a,b):
    print(a+b)


add(1,2)