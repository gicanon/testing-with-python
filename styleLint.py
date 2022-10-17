
# CODE SOURCE: SOFTWARE ARCHITECTURE WITH PYTHON 

# def factorial(n):
# """ Return factorial of n """
# if n == 0:
# return 1
# else:
# return n*factorial(n-1)

# Output:  File "styleLint.py", line 5
#      """ Return factorial of n """
#                                 ^
# IndentationError: expected an indented block

# modified code: IndentationError is fixed
def factorial(n):
  """ Return factorial of n """
  if n == 0:
    return 1
  else:
    return n*factorial(n-1)