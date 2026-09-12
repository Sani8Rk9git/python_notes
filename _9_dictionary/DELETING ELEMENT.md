**DELETING ELEMENT**



\-> Method-1

del <dictionary\_name>\[key]

\-> this will delete the key:value pair

\-> if the key does not exist then it will show error



del <dictionary\_name>

\-> this will delete the entire dictionary

\-> no longer be able to use the <dictionary\_name>



\-> <dict>.pop(key)

&#x09;-> remove that key:value pair

&#x09;-> value of the key removed is returned

&#x09;-> <dict>.pop(key , message/value)

&#x09;	-> if the key is not found then the message is returned

&#x09;-> if the key is not found and we have not given the alternate value, then python 

&#x09;	raise an error.



\-> <dict>.popitem()

&#x09;-> it delete the key:value pair that is entered last in the dictionary

&#x09;-> the key:value pairs are removed in last in first out manner

&#x09;-> returns the deleted key:value pair as tuple



\-> <dict>.clear()

&#x09;-> it will make the dictionary empty dictionary











&#x09;

