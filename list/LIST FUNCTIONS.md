**LIST FUNCTIONS**



List functions



**-> min(<list\_name>)** ---> get the minimum element of the list

\-> max()

\-> sum()

\-> len(<list>) --> returns the number of elements in the list

\-> <list>.clear() --> removes all the items from the list













* **<list\_name>.append(<item>)**

\-> The append() method adds an item to the end of the list.

\-> It takes **exactly one element** and returns no value

\-> The append() does not return the new list, just modifies the original

\-> After append(), the length of the list will increase by 1 element only

\-> if the item provided is a list then the list is added as it is in the list object.











* **<list\_name>.extend(<list>)**

\-> extend() method is used for adding multiple elements(given in the form of list) to a list

\-> It takes exactly one list argument and returns no value

\-> It appends all the elements of the list argument to the list object on which the extend is applied

\-> add to the last of the list

\-> after the extend() , the length of the list will increase by the length of the inserted list







* **<list\_name>.sort()**

\-> The sort() function sorts the items of the list, by default in increasing order

\-> This is done **in-place** (it does not create a new list)

\-> It does not return anything

<list\_name>.sort(reverse = True)  ---> sort the list in decreasing order









* **<variable\_name> = sorted(<iterable\_sequence>)**

\-> sorted() function takes the name of the list(or other sequence) and returns a new sorted list

\-> by default, sort the elements in ascending order

&#x20;sorted(<list> , reverse = True)  ----> sort in decreasing order







* <list\_name>.index(<item>)

\-> index() function returns the index of the first matched item from the list

\-> if the given item is not in the list then it raise the ValueError exception









* <list\_name>.remove(<value>)

\-> the remove() method removes the first occurrence of given value from the list

\-> it does not return anything

\-> if there is not such item in the list then it will give error









* <list\_name\_2> = <list\_name> \* num

\-> \* operator is used to replicate a list num times

\-> it returns a new list

\-> num is an integer









* <list\_name>.pop(<index>)

\-> take one optional argument and returns a value- the item being deleted

\-> if no index is provided, pop() removes and returns the last item in the list

\-> it raises an error if the list is already empty.









* <list\_name>.reverse()

\-> reverses the items of the list

\-> this is done in-place

\-> does not create a new list



\-> <list>.count(<item>)

&#x09;-> returns the count of the item in the list

&#x09;-> if the item is not present in the list then it returns 0



\-> <list>.insert(<index> , <item>)

&#x09;-> insert the item at a given position

&#x09;-> index of the element before which then item is to be inserted

&#x09;-> if index > len(list) --> element inserted at the end

&#x09;-> if index < valid negative indexes --> element inserted in the front





\-> del <list> \[<index>]

\-> del <list> \[<start> : <stop>]

\-> del <list>

&#x09;-> remove individual items or sublist or delete the list object



