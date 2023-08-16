from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#create
We get a new record in the database.
"""

def test_create_record(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)

    repository.create("Test Album", 1960, 2)

    result = repository.all()
    assert result == [
        Album(1, "Group Therapy", 2011, 1),
        Album(2, 'Whats The Story Morning Glory', 1995, 2),
        Album(3, "Test Album", 1960, 2)
    ]

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
# See conftest.py to learn what `db_connection` is.
def test_get_all_records(db_connection):
    # Seed our database with some test data
    db_connection.seed("seeds/music_web_app.sql")
    # Create a new AlbumRepository
    repository = AlbumRepository(db_connection)

    albums = repository.all()  # Get all albums

    # Assert on the results
    assert albums == [
        Album(1, "Group Therapy", 2011, 1),
        Album(2, 'Whats The Story Morning Glory', 1995, 2),
    ]

def test_find_album(db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    repository = AlbumRepository(db_connection)
    album = repository.find(1)
    assert album == Album(1, "Group Therapy", 2011, 1)
    assert album.title == "Group Therapy"