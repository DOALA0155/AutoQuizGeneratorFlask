import MeCab
from wikipedia_data import get_word_description

def get_word_speech_list(title):
  sentence = get_word_description(title)
  tagger = MeCab.Tagger()
  elements = tagger.parse(sentence).split("\n")

  word_speech_list = []
  for element in elements:
    words = element.split("\t")
    if element not in [title, "EOS", ""]:
      word = words[0]
      speech = words[4]
      word_dictionary = {"word": word, "speech": speech}
      word_speech_list.append(word_dictionary)

  return word_speech_list

def get_quiz_sentence(title):
  word_speech_list = get_word_speech_list(title)

  quiz_sentence = ""
  proper_noun_number = 1
  answers = []

  for word_dictionary in word_speech_list:
    if "固有名詞" in word_dictionary["speech"]:
      quiz_sentence += " [問題{}] ".format(proper_noun_number)
      answers.append(word_dictionary["word"])
      proper_noun_number += 1

    else:
      quiz_sentence += word_dictionary["word"]

  return title, quiz_sentence, answers