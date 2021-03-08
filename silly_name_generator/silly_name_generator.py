import sys, random

print("Welcome to the Psych 'Sidekick Name Picker.'\n")
print("A name just like Sean would pick for Gus:\n\n")

first = ('Baby Oil', 'Bad News', 'Big Burps', 'Snakes', 'Burps')

last = ('Appleyard', 'Bigmeat', 'Johnson', 'Kingfish', 'Whipkey')

while True:
    firstName = random.choice(first)
    
    lastName = random.choice(last)
    
    print("\n")
    print(f"{firstName} {lastName}", file = sys.stderr)
    print("\n")
    
    try_again = input("\nTry again? (Press Enter else n to quit)\n ")
    
    if try_again.lower() == "n":
        break
        
input("\nPress Enter to exit.")
    
# I love Ricardo
