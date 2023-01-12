# Compulsory Task 2

# Import spacy

import spacy
nlp = spacy.load('en_core_web_md')

# Read in movies.txt file

file = open("movies.txt", "r")
descriptions = file.readlines()

# Create a function that returns a recommended movie
# Based on user watching Planet Hulk

def recommend_movie(planet_hulk):

# Create an empty dictionary "similarity dict"

    hulk_desc = nlp(planet_hulk)
    similarity_dict = {}

# Use for loop to add movie descriptions as keys in "similarity_dict"
# with the similarities as their values

    for desc in descriptions:
        similarity = nlp(desc).similarity(hulk_desc)
        similarity_dict[desc] = similarity

# Return the movie description with the maximum value

    return max(similarity_dict, key=similarity_dict.get)

# Save description of Planet Hulk as "hulk_desc"

planet_hulk = '''Will he save their world or destroy it?
    When the hulk becomes too dangerous for the Earth,
    the Illuminati trick Hulk into a shuttle and launch him into space
    to a planet where the Hulk can live in peace. Unfortunately, hulk land
    on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''

# Call the function to recommend a movie
# For a user who has watched planet hulk

recommended_movie = recommend_movie(planet_hulk)
print(f"Watch next...\n\n{recommended_movie}")


