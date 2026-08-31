**STRING FUNCTION**



strings are immutable



\-> len(<string>) : return the count of the characters of the string passed as argument



\-> <string>.capitalize() : returns a copy of the string with its first character capitalize



\-> <string>.count(<substring>)

&#x09;-> returns the number of occurrences of the substring in the string

&#x09;-> <string>.count(<substring> , <start> , <end>)

&#x09;	-> returns the number of occurrences of the substring in the string between

&#x09;		the given indexes of the string

&#x09;-> <string>.count(<substring> , <start>)



\-> <string>.index(<substring>)

&#x09;-> returns lowest index where the substring is found

&#x09;-> if substring is not found --> raises an exception

&#x09;-> can also provide range between which the substring is to be find

&#x09;	-> <string\_name>.index(<substring>, <start> , <end>)



**->** <string\_name>.isalnum()

&#x09;-> it returns True if all characters in the string are alphabets and numbers and 

&#x09;	there is at least one character.

&#x09;-> space is not treated as alphanumeric

&#x09;-> returns false otherwise



**->** <string\_name>.isdigit()

&#x09;-> it returns True if all characters in the string are digits and

&#x09;	there is at least one character.

&#x09;-> returns false otherwise



\-> <string\_name>.lower()

&#x09;-> it returns a copy of the string converted to lowercase



\-> <string\_name>.islower()

&#x09;-> it returns True if all characters are lower case.

&#x09;-> there is at least one character 

&#x09;-> false otherwise



\-> <string\_name>.isspace()

&#x09;-> it returns True if there is only whitespace characters in the string.

&#x09;-> there is at least one character

&#x09;-> false otherwise



\-> <string\_name>.isupper()

&#x09;-> it returns True if all characters are upper case.

&#x09;-> there is at least one character

&#x09;-> false otherwise



\-> <string\_name>.upper()

&#x09;-> it returns a copy of the string converted to upper case



\-> <string\_name>.split(<string/character>)

&#x09;-> it splits a string based on given string or character

&#x09;-> it returns a list containing split strings as members

&#x09;-> if we do not provide any argument to split , then **by default** it will split the given string considering **whitespace** as a separator

&#x09;-> if we provide a string or a character as an argument to split(), then the given string is divided into parts considering the given string as separator and **separator character is not included in the split string.**





**->** <string\_name>.isalpha()

\-> it returns True if all characters in the string are alphabetic and there is at least one character

\-> returns false otherwise



\-> <string\_name>.strip()

&#x09;-> returns a copy of the string with leading and trailing whitespaces 

&#x09;	removed(whitespaces from the leftmost and the rightmost ends are removed)

&#x09;-> <string\_name>.strip(<string>)

&#x09;	-> this returns a string with leading(start) and trailing(end) <string>

&#x09;		removed

&#x09;	-> <string> is not prefix and suffix

&#x09;		-> all combinations of the characters of the string will be removed

&#x09;			from start and end of the <string\_name>





\-> <string>.join(<string/iterable>)

&#x09;-> it joins a string/character after each member of the string provided not after the 

&#x09;	last character and not before the first character.

&#x09;-> if the provided sequence is a list/tuple then the given string/character is joined 

&#x09;	with each member of the list/tuple ----> but the list/tuple must contain all 

&#x09;	the members as string

&#x09;-> basically we need to provide a string based iterable



\-> <string\_name>.rstrip()

&#x09;-> returns a copy of the string with the whitespaces removed from the rightmost end

&#x09;-> can also provide the string as in the strip function



\->  <string\_name>.lstrip()

&#x09;-> returns a copy of the string with the whitespaces removed from the leftmost end

&#x09;-> can also provide the string as in the strip function



\-> <string\_name>.find(<substring>)

&#x09;-> returns the lowest index in the string where the substring is found

&#x09;-> return -1 if not found

&#x09;-> can also provide range between which the substring is to be find

&#x09;	-> <string\_name>.find(<substring>, <start> , <end>)



\-> <string\_name>.startswith(<substring>)

&#x09;-> returns True if the string start with the substring

&#x09;-> otherwise False



\-> <string\_name>.endswith(<substring>)

&#x09;-> returns True if the string end with the substring

&#x09;-> otherwise False



\-> <string\_name>.title()

&#x09;-> returns a title-cased version of the string where all words start with uppercase

&#x09;	characters and all remaining letters are in lowercase.



\-> <string\_name>.istitle()

&#x09;-> returns True if the string has a title case

&#x09;-> otherwise False



\-> <string\_name>.replace(<old\_substring> , <new\_substring>)

&#x09;-> returns a copy of the string with all the occurrences of the old substring 

&#x09;	replaced by new string(substring)



\-> <string>.partition(<separator/string>)

&#x09;-> splits the string at the first occurrence of separator

&#x09;-> returns a tuple containing 3 items:

&#x09;	-> part before separator

&#x09;	-> separator itself

&#x09;	-> part after separator



\-> <string\_name>.removeprefix(<substring>)

&#x09;-> returns the string without the prefix

&#x09;-> If the <substring> isn't present, a copy of the original string will be returned.

&#x09;-> <string\_name>\[len(<substring>):]



\-> <string\_name>.removesuffix(<substring>)

&#x09;-> returns the string without the suffix

&#x09;-> If the <substring> isn't present, a copy of the original string will be returned.

&#x09;-> <string\_name>\[:-len(substring)]























