# 🔥 ERDAL'S HOMEWORK — LEVEL UP SET

## Problem 1: Grade Calculator 📊

Ask the user to enter student names and scores until they type "done". Store everything in a dictionary. Then print each student with their letter grade, plus the class average at the end.

**Hints:**
- Use `while True:` with a `break` when input is "done"
- Use `float()` to convert the score
- Write a function `get_letter_grade(score)` that returns "A" (90+), "B" (80+), "C" (70+), "D" (60+), or "F"
- Use `sum(scores.values()) / len(scores)` for the average

**Expected Output:**
~~~
Enter student name (or 'done'): Alice
Enter score for Alice: 92
Enter student name (or 'done'): Bob
Enter score for Bob: 74
Enter student name (or 'done'): Carol
Enter score for Carol: 85
Enter student name (or 'done'): done
--- Report Card ---
Alice: 92.0 (A)
Bob: 74.0 (C)
Carol: 85.0 (B)
Class average: 83.67
~~~

## Problem 2: Letter Frequency Analyzer 🔤

Ask the user for a word or sentence. Count how many times each LETTER appears (ignore spaces, ignore case). Print the letters sorted from most to least frequent, and print a bar of `*` symbols next to each count.

**Hints:**
- Loop through the string with `for char in text:`
- Skip spaces with `if char == " ": continue`
- Use `.get(char, 0) + 1` just like the word counter
- Use `sorted()` with `key=lambda x: x[1], reverse=True`
- Print the bar with `"*" * count`

**Expected Output:**
~~~
Enter text: hello world
--- Letter Frequencies ---
l → 3 ***
o → 2 **
h → 1 *
e → 1 *
w → 1 *
r → 1 *
d → 1 *
~~~

## Problem 3: Inventory Shop System 🛒

Start with this dictionary:

~~~python
inventory = {"sword": 3, "shield": 5, "potion": 10}
~~~

Let the user type commands in a loop: `buy <item>`, `stock <item>`, `list`, or `quit`. Buying reduces the count by 1 (but not below 0 — print "Out of stock!" instead). `stock` shows the count for one item. `list` shows everything.

**Hints:**
- Use `.split()` to separate the command from the item name
- Write a function `buy_item(inventory, item)` and a function `show_inventory(inventory)`
- Check `if item in inventory:` before doing anything — print "Item not found!" otherwise
- Use `while True:` and `break` on "quit"

**Expected Output:**
~~~
Command: buy sword
You bought a sword! 2 left.
Command: buy axe
Item not found!
Command: stock potion
potion: 10 in stock
Command: buy sword
You bought a sword! 1 left.
Command: list
sword: 1
shield: 5
potion: 10
Command: quit
Goodbye!
~~~