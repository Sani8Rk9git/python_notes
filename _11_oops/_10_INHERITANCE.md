**INHERITANCE**



\-> when there are multiple classes, there is two types of relationship between them:

&#x09;-> Aggregation

&#x09;-> Inheritance



\-> Aggregation

&#x09;-> one class is the owner of the other class

&#x09;-> "has a" relationship

&#x09;-> Ex: Customer has a Address

&#x09;	-> Customer class is the owner of the Address class

&#x09;	-> we create a separate class for Address as it is itself a complex entity

&#x09;-> we pass an object of a class in the constructor of another class and that class

&#x09;	uses the object 

&#x09;-> we cannot access the private variables of a class in aggregation

&#x09;	-> can only access using the getter function

&#x09;-> In the aggregation class diagram we draw the two classes and join them with a line

&#x09;	and has a diamond on the line of the class that owns other class



\-> Inheritance

&#x09;-> The child class can use the attributes and methods of the parent class

&#x09;-> help in code reusability

&#x09;	-> DRY (Do not repeat yourself)

&#x09;-> to make a class child of another class

&#x09;	-> class A:

&#x09;	

&#x09;	-> class B(A):

&#x09;	-> now B becomes the child of class A

&#x09;-> now when an object of the child class is created it can access its class members

&#x09;	as well as its parent class members

&#x09;-> the child class inherit 

&#x09;	-> Constructor

&#x09;	-> Non private attributes

&#x09;	-> Non private methods

&#x09;-> if the child class has a constructor in it, then its object uses its own, but if

&#x09;	the child class does not has, then it use the constructor of the parent class

&#x09;-> in the class diagram the parent and child class are joined with a line

&#x09;	-> a triangle is present on the side of the parent class

&#x09;-> child cannot directly access private members of the parent class

&#x09;	-> it is accessed using a getter function













&#x09;















