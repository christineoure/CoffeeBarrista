#creating a coffee Barista!!

print("Hello, welcome to SmorkieHot Coffee!!!!")

name = input("What is your name?\n\n")

if name == "Ben":
  print("Your'e not welcome here evil Ben, get out!")
else:
  print("Hello " + name + " thank you so much for coming in today.\n\n")

menu = "Black Coffee, Espresso, Latte, Cappucino"

print(name +", what would you like from our menu today? Here is what we are serving.\n\n" + menu)

order = input()

price = 8

quantity = input("How many coffees would you like?\n")

total = price * int(quantity)

print("Thank you. Your total is: $" + str(total))

#print(total)

print("Sounds good " + name + ", we'll have your " + quantity + "" + order + " ready for you in a moment!")
