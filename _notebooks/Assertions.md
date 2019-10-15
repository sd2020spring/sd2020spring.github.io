---
date: 2018-11-07T18:19:09-05:00
source: notebooks/Assertions.ipynb
---

{% include toc %}


# Assertions

`assert` statements are a useful debugging tool in Python (and other languages). You can insert "sanity check" assertions into your code, and Python will raise an error if they are violated:


```python
import math

def root(x):
    # NB: assert is a statement not a function, so we don't call with ()
    assert x >= 0, "Positive values only (keep it real!)"
    return math.sqrt(x)

print(root(4))
print(root(-4))
```

{: class="nb-output"}

    2.0



    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-31-9aef97c90f4b> in <module>()
          7 
          8 print(root(4))
    ----> 9 print(root(-4))
    

    <ipython-input-31-9aef97c90f4b> in root(x)
          3 def root(x):
          4     # NB: assert is a statement not a function, so we don't call with ()
    ----> 5     assert x >= 0, "Positive values only (keep it real!)"
          6     return math.sqrt(x)
          7 


    AssertionError: Positive values only (keep it real!)



Assertions make your assumptions explicit, and can be read almost like part of your documentation. In this example, you're saying, "there's no way anyone would call this function with a negative value, and it would be a problem if they did so I'd like to know about it." Assertions can also be better than just placing debugging `print` statements in your code, since the program halts when an assertion fails.

Assertions should only be used for debugging purposes, not to catch errors at runtime (use Exceptions for that instead). Assertions may be stripped from your code when it is run in optimized modes, so they cannot be relied upon for anything other than debugging.

Assertions also have a connection to Exceptions in Python: under the covers, the implementation of the [`assert` statement](https://docs.python.org/3/reference/simple_stmts.html?highlight=assert#the-assert-statement) simply raises an `AssertionError` Exception if the assertion test fails. Specifically,

```python
assert expression
```
translates to

```python
if __debug__:
    if not expression: raise AssertionError
```

## Example

As a preliminary, let's store information about a graded assignment in a structured way. We could go all out and define a custom Assignment class (perhaps using Python's new [dataclass](https://docs.python.org/3/library/dataclasses.html) decorator), and that would be a great choice if we had a lot of attributes or methods to deal with. 

On the other end of the complexity spectrum, we could use a simple dictionary:

```python
assignment = {'name': 'MP2 Computational Art', 'grade': 100}
```

or even just a tuple:
```python
assignment = ('MP2 Computational Art', 100)
```

Instead I'm going to use a [namedtuple](https://docs.python.org/3.7/library/collections.html#collections.namedtuple) (you can also read about them ["Goodies" chapter of Think Python](http://greenteapress.com/thinkpython2/html/thinkpython2020.html#sec230)), which is almost as simple to use as a tuple but has convenient named fields like a class:


```python
from collections import namedtuple
Assignment = namedtuple('Assignment', ['name', 'grade'])

# Create a new MP2 submission
work = Assignment('MP2 Computational Art', 85)
print(work)
```

{: class="nb-output"}

    Assignment(name='MP2 Computational Art', grade=85)



Let's write a function to apply a late penalty according to the course policy and return a new `namedtuple`. (Quick check: could this function be written as a modifier instead? Why or why not?) 

As a "sanity check", we include an assertion that the adjusted grade is not higher than the original grade or lower than zero:


```python
def late_penalty(assignment, days_late):
    """
    Given namedtuple Assignment and number of days_late, return
    new Assignment namedtuple with grade adjusted for late penalty.
    
    >>> a1 = Assignment('MP1', 90)
    >>> late_penalty(a1, days_late=2)
    Assignment(name='MP1', grade=70)
    """
    adjusted_grade = assignment.grade - 10*days_late
    assert 0 <= adjusted_grade <= assignment.grade
    return Assignment(assignment.name, adjusted_grade)
```

If your assumptions are met, the assertion has no effect:


```python
work = Assignment('MP2 Computational Art', 85)
late_penalty(work, 1)
```

{: class="nb-output"}




    Assignment(name='MP2 Computational Art', grade=75)




On the other hand if your assumptions are violated, the assertion triggers an error:


```python
# Late by eleven days -> 110% penalty?
late_penalty(work, 11)
```

{: class="nb-output"}


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-20-f223a24b907e> in <module>()
          1 # Late by eleven days -> 110% penalty
    ----> 2 late_penalty(work, 11)
    

    <ipython-input-17-f1c3d8902c51> in late_penalty(assignment, days_late)
          9     """
         10     adjusted_grade = assignment.grade - 10*days_late
    ---> 11     assert 0 <= adjusted_grade <= assignment.grade
         12     return Assignment(assignment.name, adjusted_grade)


    AssertionError: 



This failed assertion is helpful for debugging, here suggesting that we need to handle the special case of assignments >= 10 days late.

You can also add a helpful note to your assertion: 


```python
def late_penalty(assignment, days_late):
    adjusted_grade = assignment.grade - 10*days_late
    assert 0 <= adjusted_grade <= assignment.grade, "Adjusted grade out of range"
    return Assignment(assignment.name, adjusted_grade)

late_penalty(work, 11)
```

{: class="nb-output"}


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-22-37f67b3248a3> in <module>()
          4     return Assignment(assignment.name, adjusted_grade)
          5 
    ----> 6 late_penalty(work, 11)
    

    <ipython-input-22-37f67b3248a3> in late_penalty(assignment, days_late)
          1 def late_penalty(assignment, days_late):
          2     adjusted_grade = assignment.grade - 10*days_late
    ----> 3     assert 0 <= adjusted_grade <= assignment.grade, "Adjusted grade out of range"
          4     return Assignment(assignment.name, adjusted_grade)
          5 


    AssertionError: Adjusted grade out of range



But be careful! `assert` is a statement not a function - adding parentheses will not do what you expect it to:


```python
def late_penalty(assignment, days_late):
    adjusted_grade = assignment.grade - 10*days_late
    # WRONG: Incorrect usage of assert as a "function call" not a statement
    assert (0 <= adjusted_grade <= assignment.grade, "Adjusted grade out of range")
    return Assignment(assignment.name, adjusted_grade)
```

{: class="nb-output"}

    <ipython-input-25-817aa1c7abac>:4: SyntaxWarning: assertion is always true, perhaps remove parentheses?
      assert (0 <= adjusted_grade <= assignment.grade, "Adjusted grade out of range")




```python
late_penalty(work, 11)
```

{: class="nb-output"}




    Assignment(name='MP2 Computational Art', grade=-25)




The assertion test did not fail (why not?) and the function happily assigned a negative score. Note that Python 3 gives us a nice warning about the improper usage, but earlier versions may not.

# Summary Guidelines

 - Use assertions for debugging, and to make your assumptions as a developer explicit
 - Do not use assertions to catch runtime errors (that's what Exceptions are for)
 - `assert` is a statement, **not** a function, so don't use ()
