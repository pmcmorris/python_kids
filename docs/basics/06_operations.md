# Operations

This chapter shows how to make changes to **variables** using operations.

Source: [[05_operations.py](../../code/basics/06_operations.py)]

# What is an Operation?

Hmm, that is a good question.
To "operate" really just means to control something.
So an "operation" is just doing something to something.
For variables, what you can do will normally depend on the **type** of the variable.

Let's look at numbers first:

```
score = 0
score = 5
score = 1
score = 10
```

That equals sign `=` in the above statements is doing an **assignement** operation.
That's an action that makes one thing equal another.
You could read that last line aloud as, "Make score equal to 10".
Or in the cardboard box analogy that we used earlier, "Put the number 10 in the box labled _score_".

But what if score already had a value?
Well, sorry the old value is gone now (poof).
I hope you didn't need it.
Assigning to a variable will overwrite any old value with the new one.

Sometimes we want to overwrite values.
But more frequently we want to modify them.
One thing we like to do with numbers is add them up.
Computers are really good at math operations.
In Python, we can just use the + sign to add up numbers.

```python
score = 5 + 1
print(score) # writes out 6
```

Now we're adding up numbers `(5 + 1)` but we're still overwriting score.
That's probably not what we want if we're trying to keep score.
One way to fix that would be to use `score` on both sides of the `=` sign like this:

```python
score = 0          # start at a score of zero
score = score + 5  # increase score by 5
score = score + 1  # increase score by 1
print(score)       # writes out 6
```

Whenever a variable appears on the right hand side of the `=` sign, Python will read the current value in that variable and use that in the expression for computing the new value that it's about to assign.
Those expressions can get more elaborate if you need more complex logic.

```python
score = 0                                   # start at a score of zero
points = 3                                  # player earned three points
modifier = 2                                # player is currently earning double points
bonus = 1                                   # player earned a bonus point
score = score + modifier * (points + bonus) # complex score update
print(score)                                # writes out 8
```

Here we're updating the score but we combine several different variables to figure out how much to change it by.
We also used the `*` operator here which means multiplication.

| Operator | Effect         |
|----------|----------------|
| +        | Addition       |
| -        | Subtraction    |
| *        | Multiplication |
| /        | Division       |

There are all kinds of other operations but we won't go into all of them here.
In the code above, there was also use of some brackets `()`.
These aren't operators themselves but are used to control the order in which operations occur.
Operations inside the brackes are applied before those outside the brackets.

# One More Thing...

Remember how we had to write out a variables name twice when modifying (rather than overwriting):

```
score = score + points
```

It turn out that this pattern of doing an assignment after doing an operation with the current value is extremely common.
So common in fact that Python (and many other languages) provides some "shorthand" for doing the same thing with less typing.
Instead of typing `score` twice, we can instead use the addition assignment `+=` operator.
These two lines do exactly the same thing.

```python
score = score + points # adds points to score
score += points        # also adds points to score
```

There are many other combined assignment operators:

| Operator | Effect                      |
|----------|-----------------------------|
| +=       | Add to current value        |
| -=       | Subtract from current value |
| *=       | Multiply current value by   |
| /=       | Divide current value by     |

You don't need this shorthand to write your own programs.
But it helps to know about it when reading other people's code.

# What About Other Types?

Well these operations barely scratch the surface for numbers.
But what about String and Boolean types?
Well this chapter is already getting a bit long.
Strings should really get their own chapter.

