```
import collections
from collections import deque

<var> = deque(<iterable>)
```
- the iterable that can be send as input can be list, dictionary, tuple, string

- ``` <var>.append(<element>) ```
    - this will insert the element in the last of the deque

- ```<var>.appendleft(<element>) ```
    - this will insert the element in the beginning of the deque

- ```<var>.pop() ```
    - remove the element from the last

- ``` <var>.popleft() ```
    - remove the element from the beginning

- ``` <var>.clear() ```
    - this will make the deque empty

- ``` <var>.extend(<element>) ```
    - this add multiple elements in the deque

- ``` <var>.extendleft(<element>) ```
    - this add the elements in the beginning of the deque one by one.

- ``` <var>.rotate(<value>) ```
    - this will shift the elements
    - if the number given is negative, the elements are shifted in left value times
    - if the number given is positive, the elements are shifted in the right value times

```
<var> = deque(<iterable> , maxlen=<value>)
```
- now the maximum length of the deque will be value
- if an element is added, one element from the deque will be removed

