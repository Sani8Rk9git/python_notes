**VARIABLES**



* In python, a variable represent named location (named labels) that **refer** to a value
* Its value can be used and processed during the program run
* These are also called **symbolic variables** because these are **named labels**



Ex : marks = 90



* So for creating variables, just assign the variable name the value of appropriate type
* Python will internally **create labels referring to these values.**
* **So in python, a variable is not created until some value is assigned to it.**





marks -------> 90









\-> Variables **are not** storage containers in python



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





\-> In python



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









