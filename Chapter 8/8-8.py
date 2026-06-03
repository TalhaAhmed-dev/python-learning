def make_album(artist_name, album_name, album_count=""):

    album_info = {
        "artist name": artist_name,
        "album name": album_name
    }

    if album_count:
        album_info["album count"] = album_count

    return album_info


while True:

    print("\nType 'q' anytime to quit")

    artist_n = input("Please enter artist name: ")

    if artist_n == 'q':
        break

    album_n = input("Please enter album name: ")

    if album_n == 'q':
        break

    album_count = input("Please enter album count: \n If none hit enter")

    if album_count == 'q':
        break

    album = make_album(artist_n, album_n, album_count)

    print("\nAlbum Information:")
    print(album)

print("\nThank you for using this program")
