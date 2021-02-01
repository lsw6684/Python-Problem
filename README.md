# Python-Problem
This is just for basic theory to use Python


# Note
- **list - [] : common and mutable sequence**
- **tuple - () : only common sequence**
- [**dictionary(=object?) - {}**](#dictionary) **: consisting of values and attributes**
- [**def**](#def) **: function**
- [**for in**](#for-in) **: This is the same as used in JS, I think.**
- [**module**](#module) **: fetch some library or function, somthing like that**

### dictionary
- **adding to object**
  Object["attribute"] = Value
  ```
  SeungWon["handsome"] = True 
  ```

### def
- **How to make**
  **def** name : - the contents of the function must be intended from the next line and then written
  ```
  def say_hello :
    print("hello")
  ```

- **Argument**
  **def** hello(name) :
  ```
  def hello(name) :
    print("Hello " + name)
  ```
  ***or***
  ```
  def hello(name) :         # Note this. In this case, if you use the low version of Python,
    print("Hello", name)    # the compiler recognizes the argument after ", " as a tuple.
  ```
  - default argument
    ```
    def hello(name="anonymous") :
    ```
  - return
    ```
    def plus(a, b)
    return a + b
    ```
### for in
**for** "name" **in** "something like array"
```
for name in [1, 2, 3, 4] :
```
### module 
```
import math
or
from math import ceil         # If you use a little bit, the latter is more recommended.

```
