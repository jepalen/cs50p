import csv
import re


def get_words(filename):
 with open(filename, "r") as f:
    contents = f.read()

    contents = " ".join(contents.split())
    contents = re.sub(r"[^\w\- ]", "", contents)
    contents = re.sub(r"\-\-", " ", contents)
    return contents.split()


def save_counts(counts,filename):
 with open(filename, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Word", "Count"])
    for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        writer.writerow([word, count])

def main():
    counts: {}
    words= get_words('address.txt')
    lower_words= [word.lower() for word in words if len(word) >4]

    counts= {word: lower_words.count(word) for word in set(lower_words)}
    # Alternative without comprehensions:
    # for word in lower_words:
    #     if word in counts:
    #         counts[word] += 1
    #     else:
    #         counts[word] = 1
    save_counts(counts,'counts.csv')

main()