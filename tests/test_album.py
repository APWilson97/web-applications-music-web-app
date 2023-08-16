from lib.album import Album

"""
Album constructs with an id, title, release_year and artist_id
"""


def test_album_constructs():
    album = Album(1, "Freedom", 2000, 1)
    assert album.id == 1
    assert album.title == "Freedom"
    assert album.release_year == 2000
    assert album.artist_id == 1


"""
We can format albums to strings nicely
"""


def test_albums_format_nicely():
    album = Album(1, "Freedom", 2000, 1)
    assert str(album) == "1, Freedom, 2000, 1"
    # Try commenting out the `__repr__` method in lib/album.py
    # And see what happens when you run this test again.


"""
We can compare two identical albums
And have them be equal
"""


def test_albums_are_equal():
    album = Album(1, "Freedom", 2000, 1)
    album2 = Album(1, "Freedom", 2000, 1)
    assert album == album2
    # Try commenting out the `__eq__` method in lib/album.py
    # And see what happens when you run this test again.