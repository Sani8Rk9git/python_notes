**STRING SLICING**



\-> it means getting a part of the string



\-> <string>\[<start>:<end>:<step>]

&#x09;-> all are integers

&#x09;-> return all the characters starting from <start> index till <end> index - 1

&#x09;-> <step> value determine after what step to take the characters

&#x09;	-> default is 1

\-> <string>\[:<end>]

&#x09;-> here <start> is considered 0



\-> <string>\[<start>:]

&#x09;-> here <end> is considered length of string + 1



\-> <string>\[::-1]

&#x09;-> return every character taken backwards



\-> <string>\[::-2]

&#x09;-> return every 2 character starting from the last character(last character is

&#x09;	included)



\-> when we slice a string outside the valid index of the string, it returns an empty subsequence

&#x09;-> because empty sequence is a valid sequence

















