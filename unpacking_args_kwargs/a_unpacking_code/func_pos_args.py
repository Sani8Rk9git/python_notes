def add(*args):
    print(sum(args))

def fun(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

add(1,2,4)
fun(a=1,b=2)
