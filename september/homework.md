## Task 1 — Dictionary Lookup

Copy this into your file:

```python
capitals = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Brazil": "Brasilia",
    "Egypt": "Cairo",
    "Canada": "Ottawa"
}
```

Ask the user for a country. If it's in the dictionary, print the capital. If not, print "Never heard of it!"

Expected output:

```
Enter a country: Japan
The capital is Tokyo

Enter a country: Mexico
Never heard of it!
```

---

## Task 2 — Wrap it in a Function

Take Task 1 and wrap the lookup logic in a function called `get_capital(country)`. It should return the capital or "Never heard of it!". Call the function and print the result.

---

## Task 3 — Add a While Loop

Now add a while loop around Task 2 so the user can keep entering countries until they type "quit".

Expected output:

```
Enter a country: France
The capital is Paris

Enter a country: Japan
The capital is Tokyo

Enter a country: quit
Goodbye!
```

---

## Task 4 — New Dictionary, Same Pattern

Now do the exact same thing but with this dictionary:

```python
athletes = {
    "LeBron": "Basketball",
    "Messi": "Soccer",
    "Federer": "Tennis",
    "Serena": "Tennis",
    "Bolt": "Track"
}
```

Ask the user for an athlete name and print their sport. Wrap it in a function called `get_sport(name)`. Keep the while loop. Quit on "quit".


## Task 5 — ATM / Bank Accounts
Copy this dictionary into your file:
~~~python
accounts = {
    "alice": 500,
    "bob": 120,
    "carlos": 1000,
    "dana": 45
}
~~~
Build a mini banking system with a while loop menu. The user picks an action: deposit, withdraw, balance, or quit.
Write two functions:
- deposit(username, amount) — adds money to that account and returns the new balance.
- withdraw(username, amount) — subtracts money, but **only if they have enough**. If they don't, return "Insufficient funds!" and don't change the balance.
If the username isn't in accounts, print "No such account!" and skip the action.
Expected output:
~~~
Action (deposit/withdraw/balance/quit): balance
Username: bob
bob's balance is $120
Action (deposit/withdraw/balance/quit): withdraw
Username: bob
Amount: 200
Insufficient funds!
Action (deposit/withdraw/balance/quit): deposit
Username: bob
Amount: 80
bob's new balance is $200
Action (deposit/withdraw/balance/quit): quit
Goodbye!
~~~
💡 Hints:
- Convert the amount to a number with int(input(...)) or float(...).
- Check if username in accounts before doing anything.
- Functions can read and modify accounts directly since it's defined above them.
---

## Task 6 — Video Game Inventory (Nested Dictionaries)
Copy this dictionary into your file:
~~~python
players = {
    "Knight": {"gold": 150, "potions": 3, "level": 12},
    "Mage":   {"gold": 80,  "potions": 7, "level": 15},
    "Rogue":  {"gold": 220, "potions": 1, "level": 10}
}
~~~
This is a **dictionary of dictionaries**. Write a function get_stat(player, stat) that returns the value of a stat (like "gold" or "level") for a player. Handle two failure cases:
- If the player doesn't exist, return "No such player!"
- If the player exists but the stat doesn't, return "No such stat!"
Then write a while loop that asks for a player name and a stat, calls get_stat(), and prints the result. Quit on "quit".
Expected output:
~~~
Player: Mage
Stat: potions
Mage has 7 potions
Player: Rogue
Stat: gold
Rogue has 220 gold
Player: Wizard
Stat: gold
No such player!
Player: Knight
Stat: mana
No such stat!
Player: quit
Goodbye!
~~~
💡 Hints:
- players["Mage"] gives you back a whole inner dictionary.
- players["Mage"]["potions"] digs one level deeper.
- Check if player in players first, then if stat in players[player].
---

"