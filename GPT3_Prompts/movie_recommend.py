import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\n"

response = openai.Completion.create(
    engine="davinci-instruct-beta",
    prompt="Movie:The Godfather\nSimilar:Drama\The Godfather II\The Sopranos\Goodfellas\Peaky Blinders\The Departed\nMovie:Titanic\nSimilar:Romance\Drame\The Great Gatsby\The Revenant\Romeo and Juliet\A walk to remember\Forrest Gump\nMovie:Inception\nSimilar:Adventure\Thriller\The Prestige\The Matrix\Memento\Limitless\Oblivion\Coherence\nMovie:Interstellar\nSimilar:Sci-fi\Adventure\The Martian\Apollo 13\Gravity\Arrival\Passengers\Firefly\nMovie:Toy Story\nSimilar:Animation\Comedy\Monsters Inc\Toy Story 3\Up\Finding Nemo\The Lego Movie\Shrek\nMovie:The Avengers\nSimilar:Sci-fi\Adventure\Iron Man 3\Thor\Captain America The Winter Soldier\The Avengers Infinity War\The Avengers Endgame\The Incredible Hulk\Spiderman Homecoming\nMovie:The Notebook\nSimilar:Romance\Drama\The Fault in our stars\The Last Song\A walk to remember\Keith\Blue Valentine\Her\Titanic\nMovie:Knives Out\nSimilar:Drama\Suspense\Gone Girl\American Hustle\Great\Nightcrawler\La la land\Boyhood\The Machinist\nMovie:Avatar\nSimilar:Fantasy\Sci-fi\Donnie Darko\The Lord of the Rings\Shape of Water\Wonder Woman\Harry Potter\nMovie:The Shining\nSimilar:Horror\Thriller\IT\Don't Breathe\JAWS\A Quiet Place\The Conjuring\The Shining\The Witch\The Nun\nMovie:The Revenant\nSimilar:Adventure\Thriller\Life of Pi\Jurassic Park\Godzilla\The Mummy\Taxi Driver\Spotlight\Moonlight\Schindler's List\nMovie:Inglorious Bastards\nSimilar:Drama\War\Forrest Gump\American Sniper\Pearl Harbour\Saving Private Ryan\12 Strong\Dunkirk\The Imitation Game\Atonement\nMovie:The Last of the Mohicans\nSimilar:Adventure\War\Gladiator\Braveheart\The Patriot\The Last Samurai\The Hobbit\Troy\King Arthur\Brave\nMovie:The Lord of the Rings\nSimilar:Fantasy\Adventure\The Hobbit\The Chronicles of Narnia\Harry Potter\The Wheel of Time\The Dark is Rising\The Golden Compass\The Hunger Games\nMovie:The Ten Commandments\nSimilar:Drama\Adventure\The King's Speech\Exodus: Gods and Kings\The Bible\The Passion of the Christ\The Nativity Story\The Chronicles of Narnia\nMovie:The Girl with the Dragon Tattoo\nSimilar:Crime\Drama\Law and Order SVU\CSI\Mindhunter\The Fall\The Killing\The Great British Baking Show\The Sopranos\nMovie:Scarface\nSimilar:Crime\Drama\The Untouchables\Goodfellas\Wolf of Wall Street\The Departed\The Godfather II\The Dark Knight\The Departed",
    temperature=0.7,
    max_tokens=64,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\n"],
)
