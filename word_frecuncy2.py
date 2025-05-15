import re

def preprocess(sentence):
    pre_sentence = re.sub(r"[^A-Za-z]+", " ", sentence)
    words = pre_sentence.split()
    words = [word.lower() for word in words]
    return words

def word_frequency(sentence):
    words = preprocess(sentence)
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    words_sorted = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return words_sorted

def main():
    sentence = input("Enter a sentence: ")
    sentence_fre = word_frequency(sentence)
    print("Word Frequency:")
    for word, freq in sentence_fre:
        if freq == 1:
            print(f"{word}: {freq} time")
        else:
            print(f"{word}: {freq} times")

if __name__ == "__main__":
    main()