#Dictionary { key : value}
alien = {
    "color":"green",
    "points":"5"
}
print(alien)
print(alien["points"])
print(alien["color"])

new_points = alien["points"]

print(f"You just earned {new_points} points.")
print(f"You just earned {alien["points"]} points.")

# for adding new value in dictionary

alien["height"]="medium"

print(alien)

#Starting with empty dictionary
fatima = {}
fatima["color"]="white"
fatima["hairs"]="black"
fatima["eyes"]="dark brown"

print(fatima)
print(f"Fatima face is {fatima["color"].title()}. Fatima hairs are {fatima["hairs"].title()} \nand Fatima eyes are {fatima["eyes"].title()}")
#Modifing value
fatima["eyes"]="black"

print(f"Fatima face is {fatima["color"].title()}. Fatima hairs are {fatima["hairs"].title()} \nand Fatima eyes are {fatima["eyes"].title()}")
#deleting a key:value
del fatima["hairs"]
fatima["hairs"]="black"
#using get() to access values
fatima_hairs=fatima.get("hairs","no value assigned")
print(fatima_hairs)