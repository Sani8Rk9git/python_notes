**\_\_name\_\_**



* it is a special build-in variable in python
* python automatically create it for every .py file
* its value depend on how the file is used
* dunder method
* 



case 1:



\-> if we have created a python file (.py file)

\-> if we run this file directly python filename.py

\-> \_\_name\_\_ = "\_\_main\_\_"



\-> if we have written this condition

if \_\_name\_\_ == "\_\_main\_\_":



then the code inside this will execute





case 2:



\-> if the file is imported in another file then

\-> \_\_name\_\_ = name of the imported file

\-> then the above condition will be false and the code inside it will not work







\-> EX: suppose there are two files

calculator.py 

program.py



&#x09;-> program.py

&#x09;	import calculator

&#x09;	.	

&#x09;	.

&#x09;	.

&#x09;-> when program.py is run then first the calculator file code is run and then 

&#x09;	program file code is run



\-> when we import something in python, python run the entire code of the imported file

&#x09;-> to prevent this \_\_name\_\_ == "\_\_main\_\_" is used

&#x09;-> this is written in the imported file

&#x09;	-> this will make the code run only when the file is run directly not 

&#x09;		when it is imported



\-> 



