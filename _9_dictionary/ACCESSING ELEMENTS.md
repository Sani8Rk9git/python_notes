**ACCESSING ELEMENTS**



1. the elements of the dictionary are accessed through keys

<dictionary\_name>\[<key>]

\->this will give the value of the key

\-> if the key is not present in the dictionary then it will give the error



2\. <dictionary\_name>

\-> this will give the entire dictionary



3\. <dictionary\_name>.keys()  ---> give all the keys

&#x09;-> returns a list of the keys

&#x09;-> take no argument

4\. <dictionary\_name>.values()  ---> give all the values

&#x09;-> return a list of the values

&#x09;-> take no argument

\-> can use list() to get them in a list





5\. <dictionary\_name>.get(key,default)

\-> it will give the value of the key

\-> if the key is not present ---> if the default argument is present, it is returned ----> otherwise error



\-> <dictionary\_name>.items()

&#x09;-> returns all the items in the dictionary as a sequence of (key,value) tuples

&#x09;-> not returned in a particular order

&#x09;-> takes no argument

&#x09;->

