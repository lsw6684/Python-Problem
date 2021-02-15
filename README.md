<p align="center">
  <a href="https://www.python.org"><img src="https://raw.githubusercontent.com/willtheorangeguy/Python-Logo-Widgets/master/pythonlogogif.gif"/></a>
</p>

***This is just for basic theory to use Python***

# Contents
- [**list**](#list) - [] **: common and mutable sequence**
- **tuple - () : only common sequence**
- [**dictionary(=object?)**](#dictionary) - **{} : consisting of keys and values**
- [**def**](#def) **: function**
- [**for in**](#for-in) **: This is the same as used in JS, I think.**
- [**module**](#module) **: fetch some library or function, somthing like that**
- [**range**](#range) **: Generate a list of numbers automately**

### list
- **Indexing** 
  **a[n]** : You can think of the array
- **Slicing** : From **a** to the **b**
  ```python
  listName[a:b]
  ```
  - **[-1]** : **Last** element of list
  - **[:-1]** : **List** that **excluded** only the last element
  - **[0:-1]** : If there is [1, 2, 3, 4, 5], From the **1** to the **4**


### dictionary
- **adding to object**

  Object["key"] = Value
  ```python
  SeungWon["handsome"] = True 
  ```
- **deleting from object**

  **del** Object["key"]
  ```python
  >>> grade = {'pey':10, 'jullet':9}
  >>> del grade[pey]
  >>> print(grade)
  {'jullet':9}
  ```
- **Keys**
  ```python
  >>> a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
  >>> print(a.keys())
  (['name', 'phone', 'birth'])  
  ```
- **Values**
  ```python
  >>> print(a.values())
  (['pey', '0119993323', '1118'])
  ```

### def
- **How to make**

  **def** name : - the contents of the function must be intended from the next line and then written
  ```python
  def say_hello :
    print("hello")
  ```

- **Argument**

  **def** hello(name) :
  ```python
  def hello(name) :
    print("Hello " + name)
  ```
  ***or***
  ```python
  def hello(name) :         # Note this. In this case, if you use the low version of Python,
    print("Hello", name)    # the compiler recognizes the argument after ", " as a tuple.
  ```
  - default argument
    ```python
    def hello(name="anonymous") :
    ```
  - return
    ```python
    def plus(a, b)
    return a + b
    ```
  - &#42;
    ```python
    >>> def test(a, b, *args) :
    >>>   print(args)
    >>> test(1, 2, 3, 4, 5, 6, 7)
    (3, 4, 5, 6, 7)
    ```
### for in
**for** "name" **in** "something like array"
```python
for name in [1, 2, 3, 4] :
```
### module 
```python
import math
or
from math import ceil         # If you use a little bit, the latter is more recommended.

```
### range
```python
range(1, 6)                     # [1, 2, 3, 4, 5]
range(6)                        # [0, 1, 2, 3, 4, 5], ( = range(0, 6) )
------------------------------
marks = [1, 2, 3, 4, 5]
for test in range(len(mark)) :  # len(mark) = 5 >> test is from "0" to "4"
```
