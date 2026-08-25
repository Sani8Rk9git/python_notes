**UNDERSTANDING PYTHON OBJECTS**



str1 = "hello"

str2 = "world"



\--> everything we create in python is really an object

&#x09;-> "hello" is an object

&#x09;-> 5 is an object of type 'int'

&#x09;-> a function is also an object

&#x09;-> everything in python is an instance of a class

&#x09;-> this class define the behaviour of that object





def func():

&#x09;pass



print(type(func)) ----> <class 'function'>

&#x09;-> telling us that func is an object of the class 'function'



\--> it allow us to understand how python deals with behaviour and how it performs

&#x09;different operations





str1 + str2 ---> helloworld

&#x09;-> how am i able to do that in python

&#x09;	-> these objects are of the same type

&#x09;	-> python has implemented this behaviour in a double underscore method

&#x09;	-> the + is mapping to a double underscore method

&#x09;	-> it is defined in the string class

&#x09;	-> \_\_add\_\_()

&#x09;		-> this method define what happen when 2 strings are added

&#x09;		-> it concatenate the two strings

&#x09;-> str1.\_\_add\_\_(str2)

&#x09;	-> gives the same result



\-> str1.\_\_len\_\_()  ---> gives the same output as len(str1)



\-> every single operation, all of the behaviour that exist in python exists as all the things in python are objects

&#x09;-> the classes behind these objects have these special magic methods (dunder

&#x09;	methods)

&#x09;	-> these map to the behaviour(operators)that are used in the python code





