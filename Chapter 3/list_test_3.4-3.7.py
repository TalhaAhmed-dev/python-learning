#3-4
guest_list= ["papa", "mama","irfan baba", "nadia mama"]
print(f"Dear {guest_list[0].title()}, would like to join us over dinner?")
print(f"Dear {guest_list[1].title()}, would like to join us over dinner?")
print(f"Dear {guest_list[2].title()}, would like to join us over dinner?")
print(f"Dear {guest_list[3].title()}, would like to join us over dinner?\n")
#3-5
guest_list[0]="taha"

print(f"Dear {guest_list[0].title()}, would like to join us over dinner?")
print(f"Dear {guest_list[1].title()}, would like to join us over dinner?")
print(f"Dear {guest_list[2].title()}, would like to join us over dinner?")
print(f"Dear {guest_list[3].title()}, would like to join us over dinner?\n")

#3-6 More guest
guest_list.append("amna")
guest_list.append("zainab")
guest_list.append("maria")
guest_list.append("fatir")

print(f"Dear {guest_list[0].title()}, would like to join us over dinner?")
print(f"Dear {guest_list[1].title()}, would like to join us over dinner?")
print(f"Dear {guest_list[2].title()}, would like to join us over dinner?")
print(f"Dear {guest_list[3].title()}, would like to join us over dinner?")
print(f"Dear {guest_list[4].title()}, would like to join us over dinner?")
print(f"Dear {guest_list[5].title()}, would like to join us over dinner?")
print(f"Dear {guest_list[6].title()}, would like to join us over dinner?\n")
print(f"Dear {guest_list[7].title()}, would like to join us over dinner?\n")
#3-7
print("Unfortunately, I can only invite only two people for dinner \n")
popped_person_1 = guest_list.pop(6)
print(f"Sorry! {popped_person_1}, I can't invite you to dinner ")
popped_person_2 = guest_list.pop(5)
print(f"Sorry! {popped_person_2}, I can't invite you to dinner ")
popped_person_3 = guest_list.pop(4)
print(f"Sorry! {popped_person_3}, I can't invite you to dinner ")
popped_person_4 = guest_list.pop(3)
print(f"Sorry! {popped_person_4}, I can't invite you to dinner ")
popped_person_5 = guest_list.pop(2)
print(f"Sorry! {popped_person_5}, I can't invite you to dinner \n")
print(f"Dear {guest_list[0].title()} and {guest_list[1]}, \n\tyou are still invited.")

del guest_list[1]
del guest_list[0]
print(guest_list)



