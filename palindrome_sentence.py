import time

def unique_words(lst):
    seen = set()
    unique = []
    for word in lst:
        if word not in seen:
            seen.add(word)
            unique.append(word)
    return unique

def longest_palindrome(s):
    substring = ""
    if len(s) < 2:
        return s
    else:
        for i in range(len(s)-1):
            for j in range(len(s)-1, i, -1):
                if s[i:j+1] == s[i:j+1][::-1]:
                    if len(s[i:j+1]) > len(substring):
                        substring = s[i:j+1]
    return substring

def longest_palindrome_center(s):
    def expand(left, right):
        # 不断往两边扩展，只要左右相等
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 返回当前回文子串
        return s[left+1:right]

    result = ""
    for i in range(len(s)):
        # 情况1：中心是一个字符（奇数长度回文）
        odd = expand(i, i)
        # 情况2：中心是两个字符之间（偶数长度回文）
        even = expand(i, i+1)

        # 更新最长结果
        if len(odd) > len(result):
            result = odd
        if len(even) > len(result):
            result = even
    unique = unique_words(result)
    return unique


def longest_palindromes_brute_do_not_repeat(s):
    substrings = []
    max_len = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j + 1]
            if sub == sub[::-1]:  # 判断是否回文
                if len(sub) > max_len:
                    max_len = len(sub)
                    substrings = [sub]  # 替换掉之前的
                elif len(sub) == max_len:
                    substrings.append(sub)

    return substrings

def longest_palindromes_center_do_not_repeat(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]  # 返回回文子串

    max_len = 0
    results = []

    for i in range(len(s)):
        # 奇数中心
        p1 = expand(i, i)
        # 偶数中心
        p2 = expand(i, i + 1)

        for p in [p1, p2]:
            if len(p) > max_len:
                max_len = len(p)
                results = [p]
            elif len(p) == max_len:
                results.append(p)

    return unique_words(results)



s_test = input("Enter a string: ")
time_start = time.time()
print("Longest palindrome substring (brute force):", longest_palindrome(s_test))
time_end = time.time()
print("Time taken (brute force):", time_end - time_start)
time_start = time.time()
print("Longest palindrome substring (center expansion):", longest_palindrome_center(s_test))
time_end = time.time()
print("Time taken (center expansion):", time_end - time_start)