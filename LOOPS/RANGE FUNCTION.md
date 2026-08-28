**RANGE FUNCTION**



\-> range() function is used with the for loop

\-> It generates a list which is a special sequence type

\-> range() requires an int before which to stop the sequence, and can optionally take start and step parameters.





Common syntax :



range(<lower limit> , <upper limit>)  both should be integers

&#x09;-> it will produce a list having numbers from lower limit to upper limit - 1

&#x09;-> upper limit is not included

&#x09;-> the default step value will be +1



range(<lower limit> , <upper limit> , <step value>)

&#x09;-> all should be integers



range(<number>)

&#x09;-> it creates a list from 0 to number - 1

&#x09;-> The in operator is used to check if a value is present in a sequence and returns 

&#x09;	True and False accordingly.



STEP value :

\-> it must be integer

\-> -1 means decrease the value by 1 everytime

\-> -2 ---> decrease the value by 2 everytime

\-> +1 ---> by default ---> increase the value by 1 everytime



\-> range() objects are lazy (values are generated on request), 

\-> support all common sequence operations

\-> take up a fixed amount of memory, no matter how long the sequence specified. 





