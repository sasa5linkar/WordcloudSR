from SerbainTagger import SrbTreeTagger

wrpped = SrbTreeTagger()
sentence = "Ovo je kratka rečenica za testiranje taggera."
tagged_sentence = wrpped.lemmarizer(sentence)

print(tagged_sentence)
