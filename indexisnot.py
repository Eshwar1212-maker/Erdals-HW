

def get_capital(country):

    capitals = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Brazil": "Brasilia",
    "Egypt": "Cairo",
    "Canada": "Ottawa"
}
    capital_title = country.strip().title()
    return capitals.get(capital_title, "what is even that")


while True:
    dd = input("Enter country name (or type quit to exit): ")

    if dd.strip().lower() == "quit":
        print("Goodbye!")
        break


    result = get_capital(dd)
    print(f"{dd.strip().title()}'s capital is: {result}\n")

#Task 2 — Wrap it in a Function
#Take Task 1 and wrap the lookup logic in a function called get_capital(country). It should return the capital or "Never heard of it!". Call the function and print the result.