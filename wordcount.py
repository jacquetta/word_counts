"""Count words in file."""


# put your code here.
def count_words(file):

    lines = open(file)

    dic_words = {}
    list_words = []
    for line in lines:
        line = line.rstrip()
        list_words = line.split(" ")
        for word in list_words:
            dic_words[word] = dic_words.get(word, 0) + 1
    lines.close()
    # for word in dic_words:
    #     print(dic_words dic_words[word])
    for key, value in dic_words.items():
        print(f"{key} {value}")
    return dic_words

count_words("twain.txt")