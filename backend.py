def get_results(prefix):
    table_results = {
        "apple": 5,
        # "banana": 4,
        # "carrot": 18
    }
    return table_results

results = get_results(prefix="a")
print(results)



def count_words_in_file(file_name):
    word_counts = {}
    with open(file_name,'r') as file:
      for line in file:
        word_list = line.replace(',','').replace('\'','').replace('.','').lower().split()
        for word in word_list:
          # Adding  the word into the wordCounter dictionary.
          if word not in word_counts:
            word_counts[word] = 1
          else:
            # if the word is already in the dictionary update its count.
            word_counts[word] = word_counts[word] + 1
    return word_counts