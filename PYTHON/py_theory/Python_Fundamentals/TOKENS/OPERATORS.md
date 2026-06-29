**OPERATORS**



* These are the tokens that trigger some computation/action **when applied** to variables and other objects in the expression.
* These variables and the objects to which the computation is applied are known as **operands**
* So **operators require operands to work upon**





&#x20;Types of operators :



&#x20;	Unary operators

&#x20;                  -> These operators require only one operand to operate upon.

&#x20;                  -> they precedes an operand

&#x20;                  Ex: unary plus          +    returns the value itself

&#x20;                      unary minus         -    result is the negation of its operand

&#x20;                                                                                value



&#x20;                      bitwise complement  \~

&#x20;                      logical negation    not



Binary operators

&#x20;   -> These operators require two operands to operate upon

&#x20;

Types :



1\. Arithmetic operators :

&#x20;  Ex: Addition       +

&#x20;      Subtraction    -

&#x20;      Multiplication \*



&#x20;      Division       /   always return the result as a float value



&#x20;      Floor division //  -> whole part of the result is returned

&#x20;                         -> fractional part is truncated



&#x20;      Exponentiation \*\*    a\*\*b  (a raised to the power b)



&#x20;      Modulus operator %



2\. Bitwise operators :



* bin() function is used to get the binary representation of a number

&#x20;   Ex: Bitwise and   \&

&#x20;       Bitwise or    |

&#x20;       Bitwise xor   ^



3\. Shift operators :

&#x20;   Ex: left shift   <<

&#x20;       Right shift  >>



4\. Identity operators :



* It is used to check if both the operands refer the same object memory



&#x20;   Ex: is   (is the identity same ?)

&#x20;       is not  (is the identity not same ?)



5\. Relational operators :



* determine the relationship among different operands
* For numeric types, values are compared after removing the trailing zeroes after the decimal point in the floating point numbers
* Strings are compared on the basis of (ordering in dictionary)
* Capital letters are lesser than small letters
* Do not compare floating point numbers with == operator as they have precision limit.
* If the comparison is true , the relational expression result into Boolean True and if the comparison is false, the relational expression result into Boolean False
* 





&#x20;Ex : less than  <

&#x20;     greater than >

&#x20;     <=

&#x20;     >=

&#x20;     ==  equal to

&#x20;     !=  not equal to



6\. Logical operators :

&#x20;Ex: Logical and

* the and operator will test the second operand only when the first operand is true, otherwise ignore it



&#x20;Logical or

* The or operator will test the second operand only when the first operand is false, otherwise ignore it



7\. Assignment operators :

&#x20;Ex: =    assignment



These all are augmented assignment operators

These create a new object with the result of the operator hence maintaining the immutable types



&#x20;    /=   assign quotient

&#x20;    +=   assign sum

&#x20;    -=          difference

&#x20;    \*=

&#x20;    %=

&#x20;    \*\*=

&#x20;    //=



8\. Membership operators :

&#x20;Ex: in  (whether variable in sequence)

&#x20;    not in ( whether variable not in sequence)





&#x20;

