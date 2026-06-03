def make_sandwich(*items):
    print("\nMaking sandwich with following items:")
    for item in items:
        print(f"-{item}")
make_sandwich("beef","chicken")
make_sandwich("beef","chicken","turkey")
make_sandwich("chicken")