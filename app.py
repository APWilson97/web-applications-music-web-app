import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.artist import Artist
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

"""@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums.html', albums=albums)"""

@app.route('/albums', methods=['GET'])
def get_album_list():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums/index.html', albums=albums)

@app.route('/albums/new', methods=['GET'])
def get_album_form():
    return render_template('albums/new.html')

@app.route('/albums', methods=['POST'])
def create_new_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = int((request.form['release_year']))
    artist_id = int((request.form['artist_id']))
    repository.create(title, release_year, artist_id)
    album = repository.find(artist_id)
    return redirect(f"/albums/{album.id}")

@app.route('/albums/<album_id>', methods=['GET'])
def get_specific_album(album_id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(album_id)
    return render_template('albums/show.html', album=album)


"""@app.route('/albums/<album_id>', methods=['GET'])
def get_album(album_id):
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)
    album = album_repository.find(album_id)
    artist = artist_repository.find(album.artist_id)
    return render_template('album.html', album=album, artist=artist)"""

@app.route('/artists/<artist_id>', methods=['GET'])
def get_artist_page(artist_id):
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artist = artist_repository.find(artist_id)
    album_repository = AlbumRepository(connection)
    album = album_repository.find(artist_id)
    return render_template('artist.html', artist=artist, album=album)

@app.route('/artists', methods=['GET'])
def get_artists_list():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artists = artist_repository.all()
    return render_template('artists.html', artists=artists)

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    artist_names = [artist.name for artist in artists]
    return ', '.join(artist_names)

@app.route('/artists', methods=['POST'])
def post_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    name = request.form['name']
    genre = request.form['genre']
    repository.create(Artist(None, name, genre))
    return ''


# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
