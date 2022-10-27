# word counts

'''tokenizing a string and counting unique words'''
text = ("this is sample text with several words "
        "this is more sample text with some different words")

# solution 1
# print(text.split())
# word_counts = {}
# for word in text.split():
#     if word in word_counts:
#         word_counts[word] += 1
#     else:
#         word_counts[word] = 1
#
#
#
# print(word_counts)
# for word, count in word_counts.items():
#     print(word, count)

# solution 2 using collections

from collections import Counter

counter = Counter(text.split())
print(counter)

c = 1
for word, count in counter.items():
    print(c, word, count)
    c += 1

# dictionary method update()
country_codes = {}
country_codes.update({"South Africa": "za"})
print(country_codes)
country_codes.update({"China": "chi"})
print(country_codes)
country_codes.update(Australia="ar")
print(country_codes)
country_codes.update(Australia="au")
print(country_codes)

# dictionary comprehensions
months = {"January": 1,
          "February": 2,
          "March": 3
          }

# reverse key-value
months2 = {number: name for name, number in months.items()}
print(months2)


