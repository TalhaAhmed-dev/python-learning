#Looping through all key : values
fatima = {}
fatima["color"]="white"
fatima["hair"]="black"
fatima["eyes"]="dark brown"

for k,v in fatima.items():
    print(f"\nFatima's {k} is {v}")
#looping through all keys only

for characters in fatima.keys():
    print(characters)
#looping through all keys only cont.

favorite_languages={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
friends=['jen','phil']
for name in favorite_languages.keys():
    print(name)

    if name in friends:
        print(f"Hi {name}, I see your favorite language is {favorite_languages[name]}")
