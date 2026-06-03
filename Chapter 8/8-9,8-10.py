def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
   for i in range(len(magicians)):
       magicians[i]= f"The Great {magicians[i].title()}"

magicians = ["fafu", "bunny", "pingu"]

make_great(magicians)
show_magicians(magicians)
