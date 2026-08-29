capitals = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Brazil": "Brasilia",
    "Egypt": "Cairo",
    "Canada": "Ottawa"
}

userquestion = input("enter country name: ")

if userquestion in capitals:
    print(f"The capital is {capitals[userquestion]}")
else:

    print("not found")



#Homework — Dictionaries + Functions + While Loops (Harder Set)
#Task 1 — Dictionary Lookup
#Copy this into your file:

#capitals = {
    #"France": "Paris",
    #"Japan": "Tokyo",
    #"Brazil": "Brasilia",
    #"Egypt": "Cairo",
    #"Canada": "Ottawa"
#}
##Ask the user for a country. If it's in the dictionary, print the capital. If not, print "Never heard of it!"

#Expected output:

##Enter a country: Japan
#The capital is Tokyo

###Enter a country: Mexico
#Never heard of it!