import argparse

# Default variables
sample_prefix = "dr"
sample_limit = 10


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


def initialize_sqlite_db():
    import sqlite3
    import pandas as pd
    words = count_words_in_file("data/sample_data/shakespear.txt")
    df = pd.DataFrame.from_dict(data=words.items())
    db = sqlite3.connect("my_local.db")
    df.to_sql(name="bag_of_words", con=db, if_exists='replace')


def get_results(
    prefix, limit=5,
):
    """
    Fetch the top 'limit' words from dataset, starting with prefix.

    :param prefix: The start of the word
    :param word_counts: a word to count mapping
    :param limit: number of results to return

    :return:
        mapping of top words and their count
    """
    import logging
    import sqlite3
    import pandas as pd
    db = sqlite3.connect("my_local.db")
    sql = f'SELECT * FROM bag_of_words where "0" like "{prefix}%" ORDER BY 1 DESC LIMIT {limit}'
    df = pd.read_sql_query(sql, db)
    word_counts = df.to_dict()
    counts = word_counts["index"].values()
    words = word_counts["0"].values()
    word_map = zip(words, counts)
    top_results = {}
    for word, count in word_map:
        if word.startswith(prefix):
            top_results[word] = count
            limit = limit - 1
            if limit == 0:
                break
    return top_results


def main():
    # Argument Parser
    parser = argparse.ArgumentParser(
        description="Parses details about what game data to load."
    )
    parser.add_argument(
        "--prefix",
        dest="prefix",
        help="The prefix to recommend words for",
        default=sample_prefix,
    )
    parser.add_argument(
        "--limit",
        dest="limit",
        help="How many top results to return",
        default=sample_limit,
    )

    # Parse Arguments
    args = parser.parse_args()

    # Lookup top words in mapping
    results = get_results(prefix=args.prefix, limit=args.limit)

    print(f"Prefix: '{args.prefix}', Limit: {args.limit}.")
    for item in results:
        print(f"{item}\t({results[item]})")


if __name__ == "__main__":
    # initialize_sqlite_db()
    main()
