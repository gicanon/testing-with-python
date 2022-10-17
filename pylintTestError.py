
# SOURCE OF CODE: https://docs.pylint.org/en/1.6.0/tutorial.html

import string
 
shift = 3
choice = raw_input("would you like to encode or decode?")
word = (raw_input("Please enter text"))
letters = string.ascii_letters + string.punctuation + string.digits
encoded = ''
if choice == "encode":
  for letter in word:
    if letter == ' ':
      encoded = encoded + ' '
    else:
      x = letters.index(letter) + shift
      encoded=encoded + letters[x]
    if choice == "decode":
      for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
          x = letters.index(letter) - shift
          encoded = encoded + letters[x]

print encoded

# flake8 testing:
# codio@milanpassive-ciphermagic:~/workspace$ flake8 pylintTestError.pypylintTestError.py:5:1: W293 blank line contains whitespace
# pylintTestError.py:12:3: E111 indentation is not a multiple of 4
# pylintTestError.py:14:7: E111 indentation is not a multiple of 4
# pylintTestError.py:16:7: E111 indentation is not a multiple of 4
# pylintTestError.py:17:7: E111 indentation is not a multiple of 4
# pylintTestError.py:17:14: E225 missing whitespace around operator
# pylintTestError.py:19:7: E111 indentation is not a multiple of 4
# pylintTestError.py:23:11: E111 indentation is not a multiple of 4
# pylintTestError.py:24:11: E111 indentation is not a multiple of 4
# pylintTestError.py:26:14: W292 no newline at end of file
# codio@milanpassive-ciphermagic:~/workspace$ 