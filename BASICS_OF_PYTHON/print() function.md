**print()** function



* It is used to display output
* It is used as : **print**(<object to be printed>)
* If we are printing a string object with the print function, then it can be enclosed with either **double quotes** or **single quotes.** (Ensure that the opening and closing quotation mark are of the **same type**).





* When multiple objects are printed with the same single print function, space is automatically inserted between them by the print function while displaying.
* print() automatically insert space between items because the **default value of sep argument is space.**
* If no value of sep is given, then print() by default add space in between the items when printing.



* print() appends a newline character at the end of the line unless we give our own end argument. (means that python automatically add a newline character in the end of a

&#x20;             line printed so that the next print() prints from the next line.)

* print() by default takes the end argument as \\n







Syntax :



print(objects , \[sep=' ' or <separator-string> end='\\n' or <end-string>])

* here objects means it can be **one or multiple** comma separated objects to be printed.
* elements in the square brackets are optional
* the sep argument specifies the **separator character**
* The end argument determines the end character that will be printed at the end of the print line.







* A print() without any value or name or expression prints a blank line.





* print() automatically convert items to string and then print them. So the items/objects provided to it must be **convertible to string type**.

&#x20; -> If we are giving something to print() which directly does not appear as string, then

&#x20;    it must yield something which is string-convertible



* print(print()) returns None
* If a statement is given inside the print() then an error is raised as the statement just execute, it does not return anything.







* In python we can break any statement by putting a \\ at the end and then press enter and then continue typing in the next line. The line will be considered as the same line.

