**BASIC OPERATION ON STRING**



\-> Concatenation of strings

&#x09;-> The + operator will create a new string by joining two operand strings

&#x09;-> <string\_1> + <string\_2>

&#x09;-> original strings are not modified as strings are immutable

&#x09;

\-> Replication (repetition) of string

&#x09;-> to use \* operator with strings, we need two types of operands:

&#x09;	-> a string and a number

&#x09;-> <number> \* <string> or <string> \* <number>

&#x09;-> string operand is the string to be repeated

&#x09;-> number operand tell how many times the string is to be repeated

&#x09;-> python will create a new string

&#x09;-> Ex: 5 \* "2" ---> "22222"



\-> Comparison operators

&#x09;-> All relational operators of python apply to strings also

&#x09;-> The comparisons are based on the standard character-by-character comparison rules

&#x09;	for Unicode (dictionary order)

&#x09;-> equality and non-equality of strings (exact character matching for individual

&#x09;	letters including upper and lower cases)

&#x09;-> For comparisons like > and <

&#x09;	-> Python internally compare using ordinal values (Unicode values)

&#x09;	-> '0' to '9' ---> 48 to 57 (ordinal value)

&#x09;	-> 'A' to 'Z' ---> 65 to 90

&#x09;	-> 'a' to 'z' ---> 97 to 122

&#x09;-> ord(<string\_character>)

&#x09;	-> gives the ordinal value of the single character

&#x09;	-> this function takes a single character

&#x09;-> chr()

&#x09;	-> takes the ordinal value and returns the character associated to the value

