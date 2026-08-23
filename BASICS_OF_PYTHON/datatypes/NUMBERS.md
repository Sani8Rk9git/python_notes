**NUMBERS**



\-> Number datatypes are used to store numeric values in python.



Numbers have the following data types :



&#x20;1. Integers



* These are whole numbers
* They have no fractional part
* represented by numeric values with no decimal point
* can be positive or negative
* 2 types of integers :



&#x20; -> Integers (signed)



* **int datatype** to store any integer (big or small)
* length depend on the memory available
* normal integers
* can be positive and negative



&#x20; -> Booleans

&#x09;-> Represent truth values True and False

&#x09;-> False behave as 0

&#x09;-> True behave as 1

&#x09;-> bool(0) gives False

&#x09;-> bool(1) gives True

&#x09;-> Boolean operators use short-circuit evaluation, which means that expression on the right-hand side of the operator is only evaluated if needed.

&#x09;-> The bool function (bool()) converts any object to a Boolean value. 

&#x09;-> By default all objects return True unless defined to return False.

&#x09;-> A few built-ins are always considered False by definition:

&#x09;	-> the constants None and False

&#x09;	-> zero of any numeric type (int, float, complex, decimal, or fraction)

&#x09;	-> empty sequences and collections (str, list, set, tuple, dict, range(0))



str() function convert a value to string





&#x20;2. Floating point Numbers



&#x09;-> It is a number having fractional part

&#x09;-> It has a decimal point

&#x09;-> Python provides a built-in function

&#x09;**round(<number>,<decimal\_places>)** to round off a floating point number to a given number of decimal places.

&#x09;	-> If no number of decimal places is specified, the number is rounded off to the nearest integer and will return an int







&#x20;3. Complex numbers



* Python represent complex number in the form  a+bj
* j is underroot -1
* a is the real part
* b is the imaginary part
* both a and b are floating point numbers
* Python display complex numbers in parenthesis when it has non-zero real part
* if z = a+bj
* z.real give the real part
* z.imag give the imaginary part

