import wikipedia

def get_word_description(word):
  wikipedia.set_lang("ja")
  description = wikipedia.summary(word)
  return description