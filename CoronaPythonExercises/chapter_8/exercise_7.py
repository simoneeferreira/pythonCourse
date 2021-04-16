def make_album(artist_name, album_title, year=None):
    album_info = {'artist': artist_name, 'album': album_title}
    if year:
        album_info['year'] = year
    return album_info

album = make_album('Lady Gaga', 'Jolene', year=2012)
print(album)

album = make_album('Sher', 'Me', year=1987)
print(album)

album = make_album('Lady Gaga', 'Telephone')
print(album)