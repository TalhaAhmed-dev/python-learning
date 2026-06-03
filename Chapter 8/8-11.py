def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    great_magicians = []

    for magician in magicians:
            great_magicians.append(f"The great {magician.title()}")

    return great_magicians

magicians= ["fafu","bunny","pingu"]

show_magicians(magicians)

great_magicians= make_great(magicians[:])
show_magicians(great_magicians)