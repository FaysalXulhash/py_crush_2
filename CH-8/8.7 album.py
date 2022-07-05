def make_album(artist, title, tracks=0):
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('artcel', 'oniket-prantor')
print(album)

album = make_album('shironamhin', 'jahaji')
print(album)

album = make_album('iron maiden', 'piece of mind', tracks=8)
print(album)