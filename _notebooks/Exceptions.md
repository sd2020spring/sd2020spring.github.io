---
date: 2018-11-07T18:19:09-05:00
source: notebooks/Exceptions.ipynb
---

{% include toc %}


# Exceptions

Reference: [Exceptions in Python tutorial](https://docs.python.org/3/tutorial/errors.html)

Exceptions in Python (and other languages) are used to handle situations during program execution when something goes wrong (exceptional cases) in a controlled way.

Let's start with a motivating example from MP1, finding complementary base pairs:


```python
def complement(c):
    if c == 'A':
        return 'T'
    if c == 'T':
        return 'A'
    if c == 'C':
        return 'G'
    if c == 'G':
        return 'C'
```

Remember that functions return `None` if they reach then end without hitting a return statement, so this is equivalent to:


```python
def complement(c):
    if c == 'A':
        return 'T'
    if c == 'T':
        return 'A'
    if c == 'C':
        return 'G'
    if c == 'G':
        return 'C'
    return None
```

`complement_seq` is a client of `complement` (that is to say, it calls `complement`):


```python
def complement_seq(dna_seq):
    return ''.join(complement(b) for b in reversed(dna_seq))
```

This compact form is a "generator expression", which you can read about in the ["Goodies" chapter of Think Python](http://greenteapress.com/thinkpython2/html/thinkpython2020.html#sec225). Let's unpack it to make debugging easier:


```python
def complement_seq(dna_seq):
    result = ''
    for b in reversed(dna_seq):
        c = complement(b)
        result += c
    return result
```

Passing an invalid argument to `complement_seq` passes an invalid argument to `complement`, which raises an exception. The exception is downstream from the call to `complement`, and has an unrevealing name and message. This makes this difficult to debug.


```python
complement_seq('CAXT')
```

{: class="nb-output"}


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-37d3d1313b61> in <module>
    ----> 1 complement_seq('CAXT')
    

    <ipython-input-4-8f9fc6967dcc> in complement_seq(dna_seq)
          3     for b in reversed(dna_seq):
          4         c = complement(b)
    ----> 5         result += c
          6     return result


    TypeError: can only concatenate str (not "NoneType") to str



## Return-value-as-error
One technique (frowned on in Python) is to represent an error by an “out-of-band” value. “Out-of-band” means not in the set of valid return values for the function.


```python
def complement(c):
    if c == 'A':
        return 'T'
    if c == 'T':
        return 'A'
    if c == 'C':
        return 'G'
    if c == 'G':
        return 'C'
    return 'error'
```

`complement` callers need to know about this. If they don't know how to recover from the error, they should return an out-of-band value too. Then *their* callers need to follow this convention as well.


```python
def complement_seq(dna_seq):
    result = ''
    for b in dna_seq[::-1]:
        c = complement(b)
        if c == 'error':
            return 'error'
        result += c
    return result
```


```python
def function_that_uses_complement_seq():
    # do some stuff that computes dna_seq
    # ...
    comp_seq = complement_seq(dna_seq)
    if comp_seq == 'error':
        return 'error'
    # now the case where comp_seq didn't return an error
```

And so on, all the way up the call stack. This is getting to be a mess - lots of repeated code and opportunities to make a mistake. Let's see how we can do better.

## Exceptions

Rather than returning a value intended to indicate an error, we can **raise an exception**.


```python
def complement(c):
    if c == 'A':
        return 'T'
    if c == 'T':
        return 'A'
    if c == 'C':
        return 'G'
    if c == 'G':
        return 'C'
    raise Exception('Invalid nucleobase {!r}'.format(c))

complement('X')
```

{: class="nb-output"}


    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    <ipython-input-3-1bde63f9f552> in <module>()
         10     raise Exception('Invalid nucleobase {!r}'.format(c))
         11 
    ---> 12 complement('X')
    

    <ipython-input-3-1bde63f9f552> in complement(c)
          8     if c == 'G':
          9         return 'C'
    ---> 10     raise Exception('Invalid nucleobase {!r}'.format(c))
         11 
         12 complement('X')


    Exception: Invalid nucleobase 'X'



The exception is thrown straight through `complement`'s callers – even if they don't know about exceptions. This makes for easier debugging, since we can trace the error back to its original source.


```python
def complement_seq(dna_seq):
    result = ''
    for b in dna_seq[::-1]:
        c = complement(b)
        result += c
    return result

complement_seq('CAXT')
```

{: class="nb-output"}


    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    <ipython-input-4-962e256e1398> in <module>()
          6     return result
          7 
    ----> 8 complement_seq('CAXT')
    

    <ipython-input-4-962e256e1398> in complement_seq(dna_seq)
          2     result = ''
          3     for b in dna_seq[::-1]:
    ----> 4         c = complement(b)
          5         result += c
          6     return result


    <ipython-input-3-1bde63f9f552> in complement(c)
          8     if c == 'G':
          9         return 'C'
    ---> 10     raise Exception('Invalid nucleobase {!r}'.format(c))
         11 
         12 complement('X')


    Exception: Invalid nucleobase 'X'



## Catching (or handling) exceptions

`pay_me_a_complement` is a client of `complement_seq`.

By default, Python will display a stack trace when the user enters an invalid sequence.


```python
def pay_me_a_complement():
    seq = input()
    print('The complement is', complement_seq(seq))

pay_me_a_complement()
```

{: class="nb-output"}

    ACTXG



    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    <ipython-input-5-285ae89e71a5> in <module>()
          3     print('The complement is', complement_seq(seq))
          4 
    ----> 5 pay_me_a_complement()
    

    <ipython-input-5-285ae89e71a5> in pay_me_a_complement()
          1 def pay_me_a_complement():
          2     seq = input()
    ----> 3     print('The complement is', complement_seq(seq))
          4 
          5 pay_me_a_complement()


    <ipython-input-4-962e256e1398> in complement_seq(dna_seq)
          2     result = ''
          3     for b in dna_seq[::-1]:
    ----> 4         c = complement(b)
          5         result += c
          6     return result


    <ipython-input-3-1bde63f9f552> in complement(c)
          8     if c == 'G':
          9         return 'C'
    ---> 10     raise Exception('Invalid nucleobase {!r}'.format(c))
         11 
         12 complement('X')


    Exception: Invalid nucleobase 'X'



We can however deal with exceptions programatically, and try to do something smart when an error occurs. In Python we use the `try…except` pattern to handle exceptions.

The following code normally acts exactly the same as the implementation above if the code in the `try` block runs without causing an exception.

However, if there is an exception within the `try` block, then the program skips the rest of that block and picks up at the start of the `except` block instead.


```python
def pay_me_a_complement():
    seq = input()
    try:
        print('The complement is', complement_seq(seq))
    except:
        print('Invalid DNA sequence: {}'.format(seq))
    print('done')

pay_me_a_complement()
```

{: class="nb-output"}

    CATXC
    Invalid DNA sequence: CATXC
    done



## Be Specific With Exceptions

One problem with the previous implementation is that **any** error in the try block (or any function it calls) will be caught by the `except` statement, thereby indiscrimately turning all program errors into an "Invalid DNA sequence" message. 

A naked `except` statement is equivalent to saying `except Exception`. This will catch any exception that is an instance of the class `Exception`, which is every exception in Python.

Catching overly broad exceptions like this can mask other problems in your program, and can be incredibly misleading as you're trying to debug.

In general, you should raise an exception of the appropriate type for the problem that you've encountered, being as specific as possible. Consult the full list of [built-in Exceptions](https://docs.python.org/3/library/exceptions.html) to choose an appropriate type (`ValueError` would be a reasonable choice in this situation).

You can then write a more specific `except ValueError` clause, which will catch those errors but let others pass through.

## Custom Exceptions

If you want to be extremely specific with exceptions, you can create your own specific to your application by inheriting from the base `Exception` class. This isn't always necessary (the built-in set along with debugging messages is pretty good), but can be useful for larger programs.


```python
class InvalidNucleobaseException(Exception):
    pass

def complement(c):
    if c == 'A':
        return 'T'
    if c == 'T':
        return 'A'
    if c == 'C':
        return 'G'
    if c == 'G':
        return 'C'
    raise InvalidNucleobaseException('Invalid nucleobase {!r}'.format(c))

```


```python
def pay_me_a_complement():
    seq = input()
    try:
        print('The complement is', complement_seq(seq))
    except InvalidNucleobaseException:
        print('Invalid DNA sequence: {}'.format(seq))

pay_me_a_complement()
```

{: class="nb-output"}

    CATXT
    Invalid DNA sequence: CATXT



## One more example

Using `try...catch`, we can rewrite our `complement` function more compactly as follows:


```python
def complement(c):
    pairs = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    try:  # Better to ask forgiveness than permission...
        comp = pairs[c]
    except KeyError:
        raise InvalidNucleobaseException('Invalid nucleobase {!r}'.format(c))
    return comp

print("A ->", complement("A"))
print("X ->", complement("X"))
```

{: class="nb-output"}

    A -> T



    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-19-d20d7dad2ea9> in complement(c)
          3     try:  # Better to ask forgiveness than permission...
    ----> 4         comp = pairs[c]
          5     except KeyError:


    KeyError: 'X'

    
    During handling of the above exception, another exception occurred:


    InvalidNucleobaseException                Traceback (most recent call last)

    <ipython-input-19-d20d7dad2ea9> in <module>()
          8 
          9 print("A ->", complement("A"))
    ---> 10 print("X ->", complement("X"))
    

    <ipython-input-19-d20d7dad2ea9> in complement(c)
          4         comp = pairs[c]
          5     except KeyError:
    ----> 6         raise InvalidNucleobaseException('Invalid nucleobase {!r}'.format(c))
          7     return comp
          8 


    InvalidNucleobaseException: Invalid nucleobase 'X'



In this implementation, we try to look up the argument `c` in the `pairs` dictionary. If `c` is a valid nucleobase then this works fine, but if not then the key will not be present in the dictionary, causing a `KeyError`. We then catch that `KeyError` and handle it (in this case by raising a more specific/descriptive error).

Note that we've included as little code as possible in the `try...except` block. We don't expect the creation of the `pairs` dictionary to raise an error and we're not prepared to handle it if it does, so it's not included as part of the `try` block.

This software pattern is sometimes known as "better to ask forgiveness than permission", since it plows ahead assuming the dictionary lookup will succeed (hopefully the common case) and deals with the failure if it occurs. The contrasting approach (checking that the input is valid first) is sometimes called "look before you leap":


```python
def complement(c):
    pairs = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    if c not in pairs:  # Look before you leap...
        raise InvalidNucleobaseException('Invalid nucleobase {!r}'.format(c))
    return pairs[c]
    
print("A ->", complement("A"))
print("X ->", complement("X"))
```

## Unit Testing

We can (and should) also write unit tests to make sure exceptions are raised properly. Recall that the doctest framework simply checks to see if the printed output matches, so the detailed execution trace that is printed whenever an exception is raised would be cumbersome to deal with. Fortunately, [doctest can omit parts of exception output](https://docs.python.org/3/library/doctest.html#what-about-exceptions) to simplify testing:


```python
def complement(c):
    """
    Return complementary nucleobase of 'c'.
    
    >>> complement('A')
    'T'
    >>> complement('G')
    'C'
    >>> complement('You look nice today')
    Traceback (most recent call last):
    ...
    InvalidNucleobaseException: Invalid nucleobase 'You look nice today'
    >>> complement('C')
    'G'
    
    """
    pairs = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    if c not in pairs:
        raise InvalidNucleobaseException('Invalid nucleobase {!r}'.format(c))
    return pairs[c]
    
import doctest
doctest.testmod()
#doctest.run_docstring_examples(complement, globals(), verbose=True)
```

{: class="nb-output"}




    TestResults(failed=0, attempted=4)




# Summary Guidelines

 - Use exceptions (not special return values) to deal with runtime errors in your program
 - Catch exceptions and try to do something to correct them (even if it is just presenting a helpful error message to your user)
 - Raise the most specific type of exception possible, and catch a specific type of exception (not all exceptions) to avoid masking errors
 - Wrap as little of your code in the `try...except` clause as possible, so that you don't catch more than you intended
