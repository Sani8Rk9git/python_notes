**ENCAPSULATION**



\-> we can change the values of the variables of the class from outside the class using objects

&#x09;-> we can access them from outside

&#x09;-> This is DANGEROUS

&#x09;-> this can make the code crash if wrong values are provided to the variables



\-> so we need to make the variables private

&#x09;-> this is done by putting double underscore before the name of the variables

&#x09;-> the name of the variable gets changed so cannot be accessed from outside

&#x09;	-> \_classname\_\_varname

&#x09;-> if we use \_\_<var> from outside, a new attribute will be created but the private 

&#x09;	variable is saved.



\-> we can also make the methods private

&#x09;-> put double underscore before the name of the method





\-> In python nothing is truly private

&#x09;-> it is a language created for adults





\-> we need to declare the data private

&#x09;-> now we create two methods getter and setter for each data

&#x09;-> getter show the private value outside

&#x09;-> setter change the value of the private variables from the outside





\-> So encapsulation

&#x09;-> it means hiding the attributes and methods from outside users

&#x09;-> the attributes are made private and has two methods getter and setter which expose 

&#x09;	the private attributes to the outside in a protected manner.

&#x09;-> this is done to protect the class code from unwanted changes









