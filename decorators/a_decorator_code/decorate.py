def greet(fnx):
    def mfnx():
        print("Good Morning!!")
        fnx()
        print("Thanks for using!!")
    return mfnx

@greet
def hello():
    print("Hi there")

hello()
