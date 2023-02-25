#This program is designed to recommend what to watch based on the word vector similarity of the description of movies.

import spacy

nlp = spacy.load("en_core_web_md") # specifying the model we want to use.

Hulk_description = """
Will he save their world or destroy it?
When the Hulk become stood anger ous for the Earth,
the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace.
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.
"""
Hulk_description = nlp(Hulk_description)
# We will now compare the similarity of Hulk_description and the list of movies in movies.txt to ascertain if spaCy's similarity
# model is able to distinguish between these long pieces of text.
def movies(description):
    "takes in a description of movies to get a recommendation for another movie!"
    file = open ("movies.txt", "r")
    f = file.readlines()
    data_ = [line.strip() for line in f]
  
    data_dict = {}
    # we will loop through every movie data_ and compare it with the description parameter and create a dictionary.
    for  movie in data_:
        similarity = nlp(movie).similarity(description)
        data_dict[movie] = similarity
    max_similarity = max(data_dict.values())

    # we will loop through the dictionary and check if value is the same as variable max_similarity and then print that as the recommendation
    for key, value in data_dict.items():
        if value ==  max_similarity:
            print(f"We recommended for you to watch: {key} ")
    file.close()

movies(Hulk_description)