**STRING FUNCTION**



strings are immutable





1. <string\_name>.lower()

\-> it returns a copy of the string converted to lowercase









2\. <string\_name>.split(<string/character>)

\-> it splits a string based on given string or character

\-> it returns a list containing split strings as members

\-> if we do not provide any argument to split , then **by default** it will split the given string considering **whitespace** as a separator

\-> if we provide a string or a character as an argument to split(), then the given string is divided into parts considering the given string as separator and **separator character is not included in the split string.**





**3.** <string\_name>.isalpha()

\-> it returns True if all characters in the string are alphabetic and there is at least one character

\-> returns false otherwise







4\. <string\_name>.strip()

\-> returns a copy of the string with leading and trailing whitespaces removed(whitespaces from the leftmost and the rightmost ends are removed)





5\. <string/character>.join(<string/iterable>)

\---> it joins a string/character after each member of the string provided not after the last character and not before the first character

\----> if the provided sequence is a list/tuple then the given string/character is joined with each member of the list/tuple ----> but the list/tuple must contain all the members as string

\----> basically we need to provide a string based iterable



6\. <string\_name>.rstrip()

\-> returns a copy of the string with the whitespaces removed from the rightmost end







7\. <string\_name>.find(<substring>)

\-> returns the lowest index in the string where the substring is found 

\-> return -1 if not found

\-> can also provide range between which the substring is to be find





