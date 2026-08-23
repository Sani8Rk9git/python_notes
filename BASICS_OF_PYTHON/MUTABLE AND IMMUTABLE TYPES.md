**MUTABLE AND IMMUTABLE TYPES**



* Python data objects are classified into two types : 



&#x20;1. Immutable types (non-modifiable types)



* These never change their values in place
* Changing in place means that modifying the same value in the same memory location
* Ex: Number datatype , strings , tuples



p = 5



q = p                        



r = 5



here p , q, r are referring to the same immutable integer value 5 



Now p = 4 



this does not mean that integer is mutable. Now p is pointing to the another memory location storing the 4 value.

* The memory address of 5 remains the same





&#x20;2. Mutable types



* Their values can be changed in place
* Ex: lists , set , dictionary
* In the same memory address, new value can be stored as and when needed.





