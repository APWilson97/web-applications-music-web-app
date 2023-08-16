from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

def test_albums_index_page(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    page.goto(f"http://{test_web_address}/albums")
    headline = page.locator('List of Albums')
    list_tag = page.locator('li')
    expect(list_tag).to_have_text([
        "Group Therapy",
        "Whats The Story Morning Glory"
        ])

"""Given a POST request to add a new book to the list
We should be able to create a book and see it reflected in the list"""

def test_albums_create_book_page(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click('text=Add a new album')
    page.fill("input[name='title']", "Love Deluxe")
    page.fill("input[name='release_year']", "1992")
    page.fill("input[name='artist_id']", '3')
    page.click("text=Create Album")

    title_element = page.locator('.t-title')
    release_year_element = page.locator('.t-release-year')
    artist_id_element = page.locator('.t-artist-id')
    expect(title_element).to_have_text('Title: Love Deluxe')
    expect(release_year_element).to_have_text('Released: 1992')
    expect(artist_id_element).to_have_text('Artist ID: 3')

"""def test_get_albums_html(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums")
    tag = page.locator('div')
    expect(tag).to_have_text([
        "Group Therapy", 
        "Whats The Story Morning Glory"
        ])"""

"""When we have a GET /albums/index request
We should see a list of albums with links attached to them"""

"""def test_get_album_id_1(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums/1")
    headline = page.locator('h1')
    paragraph = page.locator('p')
    expect(headline).to_have_text("Group Therapy")
    expect(paragraph).to_have_text([
        "Release year: 2011 Artist: Taylor Swift"
        ])"""

"""def test_get_album_id_2(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums/2")
    headline = page.locator('h1')
    paragraph = page.locator('p')
    expect(headline).to_have_text("Whats The Story Morning Glory")
    expect(paragraph).to_have_text([
        "Release year: 1995 Artist: Above and Beyond"
        ])"""

"""def test_go_to_album_1(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click('text= Group Therapy')
    h1 = page.locator('h1')
    paragraph = page.locator('p')
    expect(h1).to_have_text("Group Therapy")
    expect(paragraph).to_have_text("Release year: 2011 Artist: Taylor Swift")"""

"""def test_go_to_album_1_and_back(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click('text= Group Therapy')
    page.click('text= Go back to Albums List')
    tag = page.locator('div')
    expect(tag).to_have_text([
        "Group Therapy", 
        "Whats The Story Morning Glory"
        ])"""

"""Given an artist id
We should see a page with the artist's details"""

def test_get_artist_1(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    page.goto(f"http://{test_web_address}/artists/1")
    h1 = page.locator('h1')
    paragraph = page.locator('p')
    expect(h1).to_have_text('Taylor Swift')
    expect(paragraph).to_have_text('Album: Group Therapy Genre: Pop')

"""Given a get request of GET /artists
We should see a page of artists with their links"""

def test_get_artist_page(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    page.goto(f"http://{test_web_address}/artists")
    tag = page.locator('div')
    expect(tag).to_have_text([
        "Taylor Swift",
        "Above and Beyond"
        ])

"""When shown an artist page
We should be able to go back to /artists"""

def test_get_artist_page_and_go_back(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    page.goto(f"http://{test_web_address}/artists")
    page.click('text= Taylor Swift')
    page.click('text= Go back to Artists page')
    tag = page.locator('div')
    expect(tag).to_have_text([
        "Taylor Swift",
        "Above and Beyond"
        ])

"""When we click on an artist
We should see the artist/artist_id page as a response"""

def test_go_to_artist_1_page(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    page.goto(f"http://{test_web_address}/artists")
    page.click('text= Taylor Swift')
    h1 = page.locator('h1')
    paragraph = page.locator('p')
    expect(h1).to_have_text('Taylor Swift')
    expect(paragraph).to_have_text('Album: Group Therapy Genre: Pop')

# === End Example Code ===
