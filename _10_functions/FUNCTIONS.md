**FUNCTIONS**





\-> In Python, units of functionality are encapsulated in functions

&#x09;-> a function is a code that has a name and it can be reused (executed again)

&#x09;	by specifying its name in the program when needed

&#x09;-> functions are objects also

&#x09;-> Functions can be executed by themselves, passed as arguments to other

&#x09;	functions, nested, or bound to a class.

&#x09;-> When functions are bound to a class name, they're referred to as methods.

&#x09;-> The def keyword begins a function definition.

&#x09;-> Each function can have zero or more formal parameters in () parentheses,

&#x09;	followed by a : (colon)

&#x09;-> Statements for the body of the function begin on the line following def

&#x09;	and must be indented in a block.

&#x09;-> Functions explicitly return a value or object via the return keyword

&#x09;	-> Functions that do not have an explicit expression following a

&#x09;		return will implicitly return the None object.

&#x09;	-> Functions that omit return will also implicitly return the None

&#x09;		object.

&#x09;		-> This means that if you do not use return in a function, Python

&#x09;			will return the None object for you.

&#x09;-> Functions are called or invoked using their name followed by ()

&#x09;	-> **Calling of a function becomes a statement** (so the code is executed)

&#x09;	-> Dot (.) notation is used for calling functions that are defined inside

&#x09;		inside a class or module.





\-> Types of arguments

&#x09;-> default argument 

&#x09;	-> we give some default value to the function parameter

&#x09;	-> if the function call is not provided with the arguments, these default

&#x09;		parameters will be assigned

&#x09;-> positional arguments

&#x09;	-> the arguments go to the function parameter in order

&#x09;	-> one argument to parameter at first position, ...

&#x09;	-> 

&#x09;-> keyword arguments

&#x09;	-> we send the arguments to the function with the name of the parameters

&#x09;	-> remember when we use functions in pandas and any other library

&#x09;		we use parameter name and then pass a value

&#x09;-> 



\-> functions are independent programs 

\-> nested function is a function inside another function

&#x09;-> same variable can be used in all the nested functions

&#x09;-> since they are independent programs, each variable has different scopes



a = 3

b = a

b ---> 3



def func():

&#x09;#code



x = func



x()



\-> we can store the function inside a list

\-> functions behave as datatype in python



\-> we can return a function through another function

&#x09;-> when a function f returns another function x

&#x09;-> we can call both functions in a single line

&#x09;-> f() (val1 , val2)

&#x09;-> 





\-> we can also sent function as argument for another function



\-> functions act like datatypes

&#x09;-> the work that can be done with the datatype can be done with the functions















