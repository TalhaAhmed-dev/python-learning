guests = ["Imran Khan", "Elon Musk", "Muhammad Ali"]

print(guests[0] + ", I would like to invite you to dinner.")
print(guests[1] + ", I would like to invite you to dinner.")
print(guests[2] + ", I would like to invite you to dinner.")
guests = ["Imran Khan", "Elon Musk", "Muhammad Ali"]

print("Elon Musk can't make it.\n")

guests[1] = "Bill Gates"

print(guests[0] + ", I would like to invite you to dinner.")
print(guests[1] + ", I would like to invite you to dinner.")
print(guests[2] + ", I would like to invite you to dinner.")
guests = ["Imran Khan", "Bill Gates", "Muhammad Ali"]

print("Good news! I found a bigger dinner table.\n")

guests.insert(0, "Cristiano Ronaldo")
guests.insert(2, "Mark Zuckerberg")
guests.append("Lionel Messi")

print(guests[0] + ", I would like to invite you to dinner.")
print(guests[1] + ", I would like to invite you to dinner.")
print(guests[2] + ", I would like to invite you to dinner.")
print(guests[3] + ", I would like to invite you to dinner.")
print(guests[4] + ", I would like to invite you to dinner.")
print(guests[5] + ", I would like to invite you to dinner.")
guests = ["Imran Khan", "Bill Gates", "Muhammad Ali"]

print("Good news! I found a bigger dinner table.\n")

guests.insert(0, "Cristiano Ronaldo")
guests.insert(2, "Mark Zuckerberg")
guests.append("Lionel Messi")

print(guests[0] + ", I would like to invite you to dinner.")
print(guests[1] + ", I would like to invite you to dinner.")
print(guests[2] + ", I would like to invite you to dinner.")
print(guests[3] + ", I would like to invite you to dinner.")
print(guests[4] + ", I would like to invite you to dinner.")
print(guests[5] + ", I would like to invite you to dinner.")
guests = ["Cristiano Ronaldo", "Imran Khan", "Mark Zuckerberg",
          "Bill Gates", "Muhammad Ali", "Lionel Messi"]

print("Unfortunately, I can invite only two people for dinner.\n")

removed_guest = guests.pop()
print("Sorry " + removed_guest + ", I can't invite you.")

removed_guest = guests.pop()
print("Sorry " + removed_guest + ", I can't invite you.")

removed_guest = guests.pop()
print("Sorry " + removed_guest + ", I can't invite you.")

removed_guest = guests.pop()
print("Sorry " + removed_guest + ", I can't invite you.")

print("\nYou are still invited:")
print(guests[0])
print(guests[1])

del guests[0]
del guests[0]

print("\nFinal guest list:", guests)
