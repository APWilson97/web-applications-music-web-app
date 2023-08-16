from lib.artist import Artist

"""
Artist constructs with an id, name and genre
"""


def test_artist_constructs():
    artist = Artist(1, "Taylor Swift", "Pop")
    assert artist.id == 1
    assert artist.name == "Taylor Swift"
    assert artist.genre == "Pop"


"""
We can format artists to strings nicely
"""


def test_artists_format_nicely():
    artist = Artist(1, "Taylor Swift", "Pop")
    assert str(artist) == "Artist(1, Taylor Swift, Pop)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.


"""
We can compare two identical artists
And have them be equal
"""


def test_artists_are_equal():
    artist = Artist(1, "Taylor Swift", "Pop")
    artist2 = Artist(1, "Taylor Swift", "Pop")
    assert artist == artist2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.