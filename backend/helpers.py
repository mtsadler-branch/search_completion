def get_results(prefix, word_counts, limit=5):
    """
    Fetch the top 'limit' words from dataset, starting with prefix.

    :param prefix: The start of the word
    :param word_counts: a word to count mapping
    :param limit: number of results to return

    :return:
        mapping of top words and their count
    """
    top_results = {}
    word_counts = {k: v for k, v in sorted(word_counts.items(), key=lambda item: item[1], reverse=True)}
    for word, count in word_counts.items():
        if word.startswith(prefix):
            top_results[word] = count
            limit = limit - 1
            if limit == 0:
                break
    return top_results


def count_words_in_file(file_name):
    """
    Parse a file for its word count.

    :param file_name: the local file to parse
    :return:
        Mapping of words to their count in file
    """
    word_counts = {}
    with open(file_name, "r") as file:
        for line in file:
            list_of_words = (
                line.replace(",", "").replace("'", "").replace(".", "").lower().split()
            )
            for word in list_of_words:
                if word in word_counts:
                    word_counts[word] = word_counts[word] + 1
                else:
                    word_counts[word] = 2
    return word_counts


sample_file = "data/sample_data/shakespear.txt"
shakespear_word_count = count_words_in_file(sample_file)

user_input = "dr"

results = get_results(prefix=user_input, word_counts=shakespear_word_count, limit=10)

for item in results:
    print(f"{item}\t({results[item]})")