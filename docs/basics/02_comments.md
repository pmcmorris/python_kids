# Comments

This chapter shows how to use comments.
**Comments** are notes that programers leave in the code for people to read.

Source: [[02_comments.py](../../code/basics/02_comments.py)]

# What is a Comment?

Have you ever played the game "Simon Says"?
Well, it's a game where you try to trick the players into doing something they weren't supposed to do.
When players are _supposed_ to do something, the sentence will start with "Simon Says ...".
Like this:

```
Simon says, pat your tummy.
```

But if someone says:

```
Pick your nose.
```

Then I sure hope you didn't listen.

The part that something starts with is called a **prefix**.
When players are _not_ supposed to do something, the sentence will not have the special "Simon says" prefix.

Computer programs are a bit like that game.
Some lines contain **commands** that the computer should **execute** (that means run them).
While other lines contain **comments** that the computer should ignore.

In the game, all commands are _prefixed_ with "Simon says" and commands have no prefix.
That is how you can tell the difference.
But in python, it's the opposite.
Comments start with a `#` character as a prefix.
This symbol has many names for some reason: Hash, Pound Sign, Number Sign, or Octothorpe.
What the heck is an Octothorpe? Well, now you know.
That's a great name to use if you don't want people to know what you're talking about.
But in this book, we'll try to use the symbol for clarity.
In Python, lines that _don't_ start with a `#` prefix are commands for the computer to execute.

```python
# This is a comment
this_is_a_command()
```

Comments don't "execute".
The Python interpreter that reads your program will just ignore them.
So they don't change the behavior of a program.

Python is a bit more complex than the Simon Says game.
You can have a command and a comment on the same line.
Anything before the `#` character is a command while anything after that character to the end of the line is a comment.

```python
this_part_is_a_command() # This part is a comment
```

When you run the example program for this chapter, the output will be the same as the program in the previous chapter.
Both write `Hello World!` to the console.
This is because even though the source file contains different text, the part that is **code** hasn't changed.
Comments aren't really code.
They're just mixed in there with the code.

# Why Use Comments?

But even if they don't do anything, they're still useful.
You can use them to help explain what the code does, how it works, or anything you think you might want to know later.

You can also use them to temporarily disable a line of code.
Put a '#' at the start of the line and it wont execute anymore.
Delete it and it will start working again.
This might be handy if the line contains something useful that you might want later and don't want to delete and lose.
