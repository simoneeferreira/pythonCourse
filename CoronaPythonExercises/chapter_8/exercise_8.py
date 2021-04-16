def make_album(artist_name, album_title, year=None):
    album_info = {'artist': artist_name, 'album': album_title}
    if year:
        album_info['year'] = year
    return album_info

while True:
    print("\nEnter artist name and album title:")
    print("(enter 'q' at any time to quit)")
    artist = input("Artist: ")
    if artist == 'q':
        break
    album = input("Album: ")
    if album == 'q':
        break

    album_info = make_album(artist, album)
    print(f"\n{album_info}")