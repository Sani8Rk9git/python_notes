**LIST SLICING**



* sub part of the list extracted out

&#x20;

<var\_name> = <list\_name>\[start:stop]

\-> both are integers

\-> stop is not included



<var\_name> = <list\_name>\[start:stop:step]

\-> all are integers



\-> if the start and stop are given beyond the list index limits in the list slice ---> python returns the elements that fall between the specified boundary -> otherwise empty list





<var\_name> = <list\_name>\[:]

\-> for index 0 to last

\-> it returns the entire list



\-> Slices can be used to overwrite one or more list elements with one or more other elements

&#x09;-> the values being assigned must be sequence

&#x09;-> if the list slice index are outside the list index then the assigned sequence 

&#x09;	elements are added at the end of the list

