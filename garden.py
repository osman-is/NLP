import spacy
"""
The horse raced past the barn fell." This sentence is a garden path sentence because the reader is initially led to believe that "raced past the barn" is a complete thought, but then the sentence takes an unexpected turn with the word "fell."

"The old man the boat." This sentence is a garden path sentence because the reader is initially led to believe that "old man" is the subject of the sentence, but then the sentence takes an unexpected turn with the word "the" which leads the reader to re-parse the sentence as "The old man who was in the boat."

"The cotton clothing is usually made of grows in Mississippi." This sentence is a garden path sentence because the reader is initially led to believe that "cotton clothing" is the subject of the sentence, but then the sentence takes an unexpected turn with the word "grows" which leads the reader to re-parse the sentence as "The cotton that clothing is usually made of grows in Mississippi."

"The chicken is ready to eat that was cooking all day." This sentence is a garden path sentence because the reader is initially led to believe that "chicken" is the subject of the sentence, but then the sentence takes an unexpected turn with the phrase "that was cooking all day" which leads the reader to re-parse the sentence as "The chicken that was cooking all day is ready to eat."

"The dog that was hit by the car limped into the yard." This sentence is a garden path sentence because the reader is initially led to believe that "the dog" is the subject of the sentence, but then the sentence takes an unexpected turn with the phrase "that was hit by the car" which leads the reader to re-parse the sentence as "The dog that was hit by the car, which limped into the yard.
"""
nlp = spacy.load("en_core_web_sm")

gardenpathSentences = ["The horse raced past the barn fell.", "The old man the boat.",
"The cotton clothing is usually made of grows in Mississippi.",
"The chicken is ready to eat that was cooking all day.",
"The dog that was hit by the car limped into the yard."]

for sentence in gardenpathSentences:

    text_ = nlp(sentence)
    for ent in text_.ents:
        print(ent.text, ent.label_)

print(spacy.explain("GPE"))
print(spacy.explain("DATE"))

"""
* The first entity I looked up was 'GPE' and the explanation was 'Countries, cities, states'.
  The entity made sense interms of the word associated with it.
  
* The second entity I looked up was 'DATE' and the explanation was 'Absolute or relative dates or periods'.
  The entity made sense interms of the word associated with it.
"""