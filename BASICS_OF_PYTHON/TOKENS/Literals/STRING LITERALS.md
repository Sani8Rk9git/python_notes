**STRING LITERALS**



* The string literal is a text enclosed in quotes.

&#x09;-> Both single characters and multiple characters can be enclosed **in any form of quotes** (single or double quotes.)

&#x09;-> We can also use single quotes(for display) in a string literal of double quotes and double quotes in a string literal of single quotes.







* Python allows to have certain **nongraphic-characters** in String values.

\-> (Nongraphic-characters are those characters that cannot be directly typed with keyboard.

Ex - backspace , tab

\-> No character is typed when these keys are pressed, only some action takes place. )

\-> Nongraphic-characters are represented using **escape sequences.**

(escape sequences are represented using a **backslash (\\)** followed by one or more characters)





* Python has 2 types of strings :



1. Single-line strings



* the normal single-quote or double-quote strings are the single line strings that must be terminated in **one line.**
* Python by default creates single-line strings with both single and double quotes.
* If no closing quotation mark is found for an opened quotation mark at the end then python will show an error.





2\. Multiline strings



* With multiline strings, a text that is spread across multiple lines can be stored as **one single string.**
* 2 ways of creating multiline strings :



&#x20;       1. In normal strings , just **add a backslash** in the end before pressing enter to

&#x20;          continue typing text on the next line.

&#x20;          -> The text will be treated as continuous and displayed in a single line.

&#x20;          -> Provide space yourself



&#x20;       2. Enclose the multiline string text with **triple single quotes** **or triple double quotes**

&#x20;          -> The text will be displayed as it is written in the quotes (in multiple lines or single lines)



&#x20;

&#x20;

* Python determine the size of the string **as the count of the characters in the string.**
* If the string literal contains any escape sequence then **the escape sequence is counted as one character.**



* For multiline strings created with triple quotes, while calculating size, EOL (end of line) character (enter) is also counted in the size.
* If multiline strings enclosed in triple quotes have backslash at the end then backslash are not counted and also the enter is not counted.





* For multiline strings created with single/double quotes and **backslash character at the end of the line ,** while calculating size , the backslash is not counted in the size of the string.



* len(<object\_name>) is used to get the size or length of the object

