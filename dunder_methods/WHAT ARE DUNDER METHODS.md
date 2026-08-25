**WHAT ARE DUNDER METHODS**



\-> dunder stand for double underscore



\-> dunder methods

&#x09;-> these are special methods (reserved methods) in python that map to some

&#x09;	kind of behaviour



\-> dunder methods (double underscore methods, also called magic methods) let you define how operators and built-in functions behave on custom types and classes in Python.



\-> \_\_init\_\_() : Acts as an initializer or constructor for a class. Python runs it automatically when you create a new object to set starting values.



\-> \_\_str\_\_() : automatically be called when we try to print an object

&#x09;-> it provides the human readable version of the object

&#x09;-> return must be written with an expression that explains your object

&#x09;-> this method is called when str(<object>) is written(called)

&#x09;-> user friendly output



\-> \_\_add\_\_() : when + sign comes it goes to the class of the object on the left and look for this method

&#x09;-> it has other parameter that represent the object on the right side of +

&#x09;-> then the specific operation is performed



\-> we need to check the type of the object passed to these methods before we perform its operation

&#x09;-> if isinstance(other , <Class\_name>):



\-> \_\_repr\_\_() : known as representation method

&#x09;-> it is used for debugging

&#x09;-> provide developer friendly output

&#x09;-> repr(<object>) can be used to trigger this method



\-> \_\_iter\_\_() and \_\_next\_\_() : these make an object iterable means the object can be used in the for loop















