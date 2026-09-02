**TRUE COPY OF THE LIST**



* If we have a list



a = \[1,2,3]



* we write

b = a

* Both a and b now refer to the same list object, if we modify any of the two ----> changes will be reflected in both





* if we want to make true copy of the list



1. <list\_name\_to\_store> = list(<list\_name>)
2. <list\_name\_to\_store> = <list\_name>.copy()
3. <list\_name\_to\_store> = <list\_name>\[:]

the last method store all the elements of the list using list slice in its copy



\-> Note after creating a copy of the list, we have two different lists 

&#x09;-> But if the original list contains elements that are again list or some other 

&#x09;	variables then if we change those elements in the copy then the original

&#x09;	list will also reflect the changes

&#x09;-> so copying a list solves the first-level referencing but not the second level 

&#x09;	referencing

&#x09;-> A shallow copy is usually enough when you want to add or remove items from one of the list objects without modifying the other. 



\-> 













