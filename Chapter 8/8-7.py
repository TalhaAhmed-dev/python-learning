def make_album(artist_name,album_name,album_count=""):
while true:
    album_info={
        'artist': artist_name,
        'album': album_name,
        'album_count':album_count
    }
    if album_count:
        album_info['album_count'] = album_count
        print(f"artist name is {artist_name} and album is {album_name} and album count is {album_count}")
        return album_info
    else:
        print(f"artist name is {artist_name} and album is {album_name}")
        return album_info
