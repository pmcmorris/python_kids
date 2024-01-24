# let make the computer do some math for us
print(1 + 1) # addition:       writes 2
print(1 - 1) # subtraction:    writes 0
print(2 * 3) # multiplication: writes 6
print(4 / 2) # division:       writes 2

# Now let's use some operations and assignment to update variables

# keep adding to score (the long way)
score = 0          # start at zero
score = score + 5  # add 5 to score
score = score + 1  # add 1 to score
score = score + 10 # add 10 to score
print(score)       # writes out 16

# keep adding to score (the short way)
score = 0          # start at zero
score += 5         # add 5 to score
score += 1         # add 1 to score
score += 10        # add 10 to score
print(score)       # writes out 16

# add to score in a complex way
score = 0                            # start at a score of zero
points = 3                           # player earned three points
modifier = 2                         # player is currently earning double points
bonus = 1                            # player earned a bonus point
score += modifier * (points + bonus) # complex score update
print(score)                         # writes out 8