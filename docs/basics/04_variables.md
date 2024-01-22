# Variables

This chapter shows how programs use **variables** to keep track of useful information.

Source: [[04_variables.py](../../code/basics/04_variables.py)]

# What is a Variable?

In programs, you often need a way to store bits of information.
For example, your player in a game might have a score.
We can store this information in something called a **variable**.
Here we set `score` to `10`.

```python
score = 10
print(score)
```

Notice that we didn't put quotes like this `"` around `score` when trying to print its value.
That will make more sense later.
The name of the variable is `score` and `10` is the value is now holds.
So if we then print it out we see this:

```
10
```

You can think of a variable like a cardboard box.
We use them for holding our stuff.
Sometimes we write a name on the outside so that we remember what it's for.
That's like a variable name.
We named the box.
The value is what goes in that box.

We can also change a variables current value.
We call them "vary-able" because they can change.
Let try changing the variables value.

```python
score = 10
print(score)
score = 20
print(score)
```

The above program will write this output:

```
10
20
```

Even though both print statements looked the same `print(score)`, the second statement printed something different because the variable was now holding a different value.

You can also make as many variables so long as you give them different names.
