**VARIABLES**



\-> In python, a variable represent named location (named labels) that **refer** to a value

&#x09;-> Its value can be used and processed during the program run

&#x09;-> These are also called **symbolic variables** because these are **named labels**

&#x09;**->** no keyword is used in creating variables or constants

&#x09;-> we can bind names (also called variables) to any type of object using the

&#x09;							assignment operator

&#x09;-> <name> = <value>

&#x09;-> A name can be reassigned (or re-bound) to different values (different object types) over its lifetime

&#x09;-> Ex : marks = 90

&#x09;	-> marks -------> 90

&#x09;**-> So in python, a variable is not created until some value is assigned to it**

&#x09;-> Variables **are not** storage containers in python

&#x09;-> variables are always written in snake\_case





Other programming languages variables :

&#x20;

&#x20;They create variables as storage containers.

&#x20;Ex:

age = 23



in memory, a memory location named age will be created and it will store the value.

If we change the value of the variable then the content will change but the memory location of the variable will not change.



&#x20;             age --> 23

address       100



age = 89





age --> 89

100





\-----------------> In python



age = 12

variable age will be created as a **label** pointing to memory location where 12 is stored





age = 34

now the label age will not be having the same location as earlier. It will now refer to memory location where 34 is stored.







* So variables in python do not have fixed location. They are just named reference
* Assigning new value to an existing variable may or may not refer to the same memory location
* It depends on the type of the new value (whether it is mutable or immutable)







&#x20;Lvalues and Rvalues



* Lvalues : expressions that come on LHS and RHS of an assignment

&#x20;            -> These are the objects to which a value or expression is assigned

* Rvalues : expressions that come on RHS of an assignment

&#x20;            -> These are the literal or expression that are assigned to the Lvalues



* variable names are Lvalues
* Assigning a value to a variable means that variable's label is referring to that value







* We can assign **same value to multiple variables** in a single line. All the labels will refer to the same location with the assigned value
* We can assign multiple values to multiple variables in single line. Python will assign the values **order wise** (first variable is given first value , second variable second value...)



NOTE: Python first evaluate RHS expressions(left to right) and then assigns them to LHS





&#x20;**Dynamic typing feature of python**



* In python, variable is defined by assigning to it some value of a particular type
* Python allows dynamic typing through which a variable pointing to a value of a certain type can be made to point to a value/object of different type.
* Since the python variables are labels associated with objects, with dynamic typing, python makes the label refer to a new value.
* We can make the variable(pointing to a value of a certain type) to point to the value of different type by just reassigning a value of that type.





type(<object name>) is used to determine the type of the object (what type of value does it point to)



* &#x20;In **static typing ,** a datatype is attached to the variable when it is defined first and it is fixed.





\---> Constants

&#x09;->Constants are names meant to be assigned only once in a program.

&#x09;-> They should be defined at a module (file) level, and are typically visible to all functions and classes in the program.

&#x09;-> Using SCREAMING\_SNAKE\_CASE signals that the name should not be re-assigned, or its value mutated.

