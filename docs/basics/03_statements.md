# Statements

This chapter shows how programs are built out of statements.
These are the parts of the program that **execute**.
They do something.

Source: [[03_statements.py](../../code/basics/03_statements.py)]

# What is a Statement?

In the previous chapter we talked about commands versus comments and said that commands do something. Let's learn how to make the computer do something.
There are many ways to give the computer commands.
Telling it to run your program is a command.
In a programming language, there are normally lots of different ways to control a computer's behavior.
A **statement** is a way of expressing in code what the computer should do.
Depending on the context what is considered a statement may have a _very_ precise definition.
Someone might say to you, "Technically, that's an expression" or "Techically, that's a directive".
For the moment, you can safely ignore anyone that starts a sentence with the prefix "Technically, ..."
A statement is code that does something.
That's as detailed as we want to get.

In the [[01_hello.py](../../code/basics/01_hello.py)] program we on used a single statement.
That statement was to call the `print` funtion (we'll explain what a function is in a minute).
But we could have used many statements.

```python
print("Hello World!") 
print("Hi there.") 
print("Hey, how ya doin?") 
```

If you ran that code, you would see this output:

```
Hello World!
Hi there.
Hey, how ya doin?
```

Read that code and see if you can figure out why it had that output.
One thing you might notice is that the order of the output matches the code.
This an important point.
Statements execute **sequentially**.
This means one after the other, in the order they appeared in the code.
Later, we'll learn how to jump somewhere else in the code so that we can control the order things execute.
Until then, our programs just execute top to bottom.
But that can still be fun.
Check out the [example](../../code/basics/03_statements.py) for this chapter to see how.
