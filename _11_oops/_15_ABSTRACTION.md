**ABSTRACTION**



\-> Abstraction in Python is the process of hiding complex internal implementation details and exposing only the essential features or interfaces to the user.



\-> Python achieves formal abstraction through the built-in abc (Abstract Base Classes) module.



\-> Abstract Base Class (ABC): A class that cannot be instantiated directly. It serves as a structural blueprint or "contract" for other classes.



\-> Abstract Method: A method declared inside an abstract class that has a definition but no implementation (typically contains just pass). Subclasses must override and implement this method.



\-> Concrete Method: A regular method with a fully functional implementation inside the abstract class. Subclasses inherit this method directly to promote code reuse.





\-> if the child class does not implement the abstract methods of the abstract class then python raises error

&#x09;-> so with abstraction, a class can force some things on the child class that 

&#x09;	inherit it.







