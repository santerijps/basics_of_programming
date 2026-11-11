name = input("Please enter your name: ")

if name == "Alice":
    print("Hi, Alice!")
elif name == "Bob": # else if
    print("What's up, Bob?")
elif name == "Charlie": # else if
    print("Yo, Bob!")
else:
    print("Who are you?")

match input("Please enter your name: "):
    case "Alice":
        print("Hi, Alice!")
    case "Bob":
        print("Hi, Bob!")
    case unrecognizedName:
        print(f"Who are you, {unrecognizedName}?")

# Trivia: other programming languages might use switch instead of match
'''
switch (name) {
    case "Alice":
        ...
        break;
    default:
        ...
}
'''
