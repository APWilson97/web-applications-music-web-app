from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""


# See conftest.py to learn what `db_connection` is.
def test_get_all_records(db_connection):
    # Seed our database with some test data
    db_connection.seed("seeds/music_web_app.sql")
    # Create a new ArtistRepository
    repository = ArtistRepository(db_connection)

    artists = repository.all()  # Get all artists

    # Assert on the results
    assert artists == [
        Artist(1, 'Taylor Swift', 'Pop'),
        Artist(2, 'Above and Beyond', 'Electronic')
    ]


"""
When we call ArtistRepository#create
We get a new record in the database.
"""


def test_create_record(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = ArtistRepository(db_connection)

    repository.create(Artist(None, "Test Artist", "Rock"))

    result = repository.all()
    assert result == [
        Artist(1, 'Taylor Swift', 'Pop'),
        Artist(2, 'Above and Beyond', 'Electronic'),
        Artist(3, "Test Artist", "Rock")
    ]