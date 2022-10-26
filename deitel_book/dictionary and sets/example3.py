# word counts

'''tokenizing a string and counting unique words'''
text = ("this is sample text with several words "
        "this is more sample text with some different words")

print(text.split())
word_counts = {}
for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1



print(word_counts)
for word, count in word_counts.items():
    print(word, count)

