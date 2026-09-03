**UNPACKING AND MULTIPLE ASSIGNMENT**



\-> Unpacking refers to the act of extracting the elements of a collection, such as a list, tuple, or dictionary, using iteration.

&#x09;-> Unpacked values can then be assigned to variables within the same statement.

&#x09;-> Ex:

&#x09;	-> for item in list

&#x09;	-> item takes on the value of each list element in turn throughout the

&#x09;		iteration.

&#x09;-> values appear within lists/tuples in a specific order, they are unpacked into

&#x09;	variables in the same order.

&#x09;-> If there are values that are not needed then you can use \_ to flag them

&#x09;-> iteration over dictionaries defaults to the keys. So when unpacking a dict, you

&#x09;	can only unpack the keys and not the values.

&#x09;	-> If you want to unpack the values then you can use the <dict>.values()

&#x09;	-> If both keys and values are needed, use the <dict>.items()

&#x09;		-> These can be unpacked into a tuple

&#x09;->

&#x09;











\-> Multiple assignment is the ability to assign multiple variables to unpacked values within one statement.

&#x09;-> This allows for code to be more concise and readable, and is done by separating

&#x09;	the variables to be assigned with a comma.

&#x09;-> Ex: first, second, third = (1,2,3)

&#x09;-> Ex: for index, item in enumerate(iterable)

&#x09;-> the number of variables on the left side of the assignment operator (=) must match

&#x09;	the number of values on the right side.

&#x09;-> To separate the values, use a comma ,

&#x09;-> If the multiple assignment gets an incorrect number of variables for the values

&#x09;	given, a ValueError will be thrown.

&#x09;-> Multiple assignment is not limited to one data type, can assign different

&#x09;	datatypes

&#x09;-> Multiple assignment can be used to swap elements





\-> The special operators \* and \*\* are often used in unpacking contexts

&#x09;-> \* can be used to combine multiple lists/tuples into one list/tuple by unpacking

&#x09;	each into a new common list/tuple.

&#x09;-> \*\* can be used to combine multiple dictionaries into one dictionary by unpacking

&#x09;	each into a new common dict.



&#x09;-> When unpacking a list/tuple you can use the \* operator to capture "leftover"

&#x09;	values.



\-> Packing

&#x09;-> Packing is the ability to group multiple values into one list that is assigned to

&#x09;	a variable.

&#x09;-> Packing a list/tuple can be done using the \* operator

&#x09;-> Packing a dictionary is done by using the \*\* operator.

&#x09;-> When you create a function that accepts an arbitrary number of arguments, you can

&#x09;	use \*args or \*\*kwargs in the function definition.

&#x09;-> \*args is used to pack an arbitrary number of positional (non-keyworded) arguments

&#x09;-> \*\*kwargs is used to pack an arbitrary number of keyword arguments.



&#x09;-> \*args and \*\*kwargs can also be used in combination with one another

&#x09;-> def my\_function(<positional\_args>, \*args, <key-word\_args>, \*\*kwargs)

&#x09;-> You can use \* to unpack a list/tuple of arguments into a function call.

&#x09;	-> This is very useful for functions that don't accept an iterable



\-> in the function definition, \* performs packing

\-> in the function call, \* performs unpacking

