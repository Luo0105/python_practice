import re
from collections import Counter

def count_word_frequency(sentence):
    cleaned_sentence = re.sub(r'[^\w\s]', '', sentence).lower()
    words = cleaned_sentence.split()
    return Counter(words)

def analyze_sentence_frequency():
    user_sentence = input("请输入一个句子：")
    word_frequency = count_word_frequency(user_sentence)
    sorted_frequency = sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)

    print("词频统计结果：")
    for word, frequency in sorted_frequency:
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    analyze_sentence_frequency()
