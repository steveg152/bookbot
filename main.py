def main():
  text = get_text()
  word_count = count_words(text)
  letters = count_letters(text)
  
  print_report(word_count, letters)

def count_words(text):
  words = text.split()
  return len(words)

def get_text():
  with open("books/frankenstein.txt") as f:
    text = f.read()
    return text
  
def count_letters(text):
  letters = {}
  for letter in text:
    lower = letter.lower()
    if lower in letters:
      letters[lower] += 1
    else:
      letters[lower] = 1
  return letters

def print_report(word_count, letters):
  print(f"Report from frankenstein.txt")
  print(f"The total number of words was {word_count}")
  sorted_letters = conver_dict_to_list(letters)
  for letter in sorted_letters:
    if letter['char'].isalpha():
      print(f" the letter { letter['char'] } was found {letter['count']} times")

def sort_on(d):
    return d["count"]

def conver_dict_to_list(letters):
  letter_list = []
  for letter in letters:
    letter_list.append({"char": letter, "count": letters[letter]})
    letter_list.sort(reverse=True, key=sort_on)
  return letter_list

main()