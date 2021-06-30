import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\n"

response = openai.Completion.create(
    engine="davinci-instruct-beta",
    prompt="Genre:Rock\nSongs:Come Together\House of Rising Sun\Paradise City\Hammer of God\Hotel California\Bohemian Rhapsody\Radioactive\Sweet child of mine\Comfortably Numb\nGenre:Romantic\nSongs:Perfect\A sky full of stars\I like me better\All of me\Thinking out loud\Hey Jude\A thousand years\Closer\Yellow\nGenre:Chill\nSongs:Cheap Thrills\Memories\Little things\At my worst\This city\Before you go\Let it be\21 guns\nGenre:Sad\nSongs:Enough for you\Falling\Train wreck\learn to let go\Another love\Memories\See you again\nGenre:Happy\nSongs:Closer\Something just like this\Uptown girl\Fireflies\The scientist\Girls Like you\I want to break free\nGenre:Pop\nSongs:Cheap Thrills\Uptown Funk\See you again\Shake it off\Counting stars\Hotline bling\Hello\nGenre:Slow\nSongs:Under the Bridge\White flag\American girls\End of the road\The fear\nGenre:Rap\nSongs:Love Yourself\Find someone\Want you bad\This is for you\Wild Things\Going crazy\Rap god\nGenre:Classic\nSongs:Infinity\Rolling in the deep\Fix you\Another brink on the wall\Billie Jean\Love me like you do\It's my life\nGenre:Metal\nSongs:Walk the Wire\Rockstar\Tears don't fall\Walk this way\Smoke on the water\Angel of death\Children of the grave\The Trooper\nGenre:Groovy\nSongs:Lose yourself\Smells like teen spirit\Single ladies\Beat It\Get Lucky\On the Floor\Cheap Thrills\Love Shack",
    temperature=1,
    max_tokens=64,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\n"],
)
