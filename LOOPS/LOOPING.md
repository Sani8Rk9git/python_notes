**LOOPING**



\-> To carry out repetitive tasks, python provides following iterative/looping statements:

&#x09;-> Conditional loop while (condition based loop/ indefinite (uncounted) iterations)

&#x09;-> Counting loop for (loop for definite(counted) iterations)



\-> The keywords **break, continue, and else** help customize loop behavior.

\-> **range() and enumerate()** help with loop counting and indexing.







For loop

&#x09;-> basic for loop go through the values of any iterable object(sequence), 

&#x09;	terminating after the last value.



Syntax :



for <variable> in <sequence>:

&#x20;   #statement to repeat



* the loop variable is assigned the value of the sequence one by one and for each assigned value the body of the loop will be executed.





\-> When there isn't a specific iterable given, the special range() sequence is used as a loop counter.

for <variable> in range():

&#x20;   #statements





\-> If both values and indexes are needed, the built-in enumerate(<iterable>) will return an iterator over (index, value) pairs



for index, word in enumerate(<sequence>):

&#x09;#code



\-> The enumerate(<iterable>) function can also be set to start the index count at a different number:



for index, word in enumerate(<sequence>, start=1):

&#x09;#code









while loop

&#x09;-> It is a conditional loop

&#x09;-> It will repeat the instructions within itself as long as the condition remains 

&#x09;	True in a Boolean context





Syntax :



while logical\_condition:

&#x20;   #loop\_body



* The variable used in the condition of the while loop must have some value before entering into while loop.

