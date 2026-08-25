**\_\_INIT\_\_.PY**





\-> when inside a folder we create and save a python file \_\_init\_\_.py , then this python

&#x09;file make that folder a python package.

&#x09;-> this allows the folder to be imported and also we can use other files that

&#x09;	are created in the folder



\-> \_\_name\_\_ and \_\_init\_\_ are called dunders (short for "double underscores") or magic methods.



\-> \_\_init\_\_.py initializes the package by running some code whenever it is imported for the first time only



\-> when we are writing a python package , this file is utilized to run some kind of setup or config before the package is fully ready or loaded and then it can be used by the python script







\-> suppose main.py has imported a package 

&#x09;-> then the package's \_\_init\_\_() file must have the complete path of the imported 

&#x09;	module otherwise it will raise Module not found error

&#x09;-> as python will look for the imported module in the directory where main.py 

&#x09;	is created



\-> .file --> one level up

\-> ..file --> two levels up



&#x20;



