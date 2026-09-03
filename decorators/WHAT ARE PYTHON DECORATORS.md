**WHAT ARE PYTHON DECORATORS ??**



\-> decorators are functions that change some other functions and then return them

&#x09;-> they modify the behaviour of functions 



\-> A decorator takes a function as an argument and returns a new function that modifies the behaviour of the original function

&#x09;-> the new function is called the decorated function



\-> The basic syntax for using the decorators is:

&#x09;-> @decorator\_function

&#x09;-> def my\_function():

&#x09;	pass



\-> The @decorator\_function notation is just a shorthand for:

&#x09;-> def my\_function():

&#x09;	pass

&#x09;-> my\_function = decorator\_function(my\_function)





