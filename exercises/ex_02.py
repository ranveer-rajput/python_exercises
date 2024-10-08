"""
# Metadata
- Level: 1
- Title: Numbers divisible by 7 but not 5
- Topics: Loops, Conditionals, List Comprehension

# Instructions
Write a function called `find_numbers(min, max)` to find list of integers which are,

- If natural number, then it should be multiple of 7 but a multiple of 5
- Otherwise, it should be a multiple of 7

Return a list of these numbers.

# How to Test
Run the following command in your terminal:

```bash
python -m unittest tests.test_ex_02
```

# Hints
- Use a loop or list comprehension to check each number in the range
- Use the modulo operator (%) to check divisibility
- Don't forget to return the list of numbers

# Notes
- Do not remove or rename `find_numbers()`, it's required and should not be altered
- You can create your own helper functions if needed
- Make sure to handle cases where min > max properly
"""


def find_numbers(min, max):

    # TODO: Implement the function to return a list of numbers between [min] and [max]
    # which are divisible by 7 but are not multiples of 5

    new_list = []

    for i in range(min, max + 1):

        if i % 7 == 0 and i % 5 != 0:
            new_list.append(i)
        elif i % 7 == 0 and i < 0:
            new_list.append(i)

    return new_list
