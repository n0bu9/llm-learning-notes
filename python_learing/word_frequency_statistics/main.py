import re
import jieba
from collections import Counter


def read_and_clean_chinese(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"error: flie {file_path} can't find")
        return ""
    except UnicodeDecodeError:
        print(f"error: file encoding not support!")
        return ""
    text = re.sub(r'[^\u4e00-\u9fa5]', '', text)
    return text


def count_words(words, stop_words=None):
    if stop_words:
        words = [words for word in words if word not in stop_words]
    counter = Counter(words)
    return counter


def display_top_words(counter, top_n=10):
    print(f"总共有 {sum(counter.values())} 个单词，其中唯一单词 {len(counter)} 个")
    print("排名 | 单词 | 频率")
    print("-" * 30)
    for rank, (word, count) in enumerate(counter.most_common(top_n), 1):
        print(f"{rank:4} | {word:12} | {count}")


if __name__ == "__main__":
    word = read_and_clean_chinese("./test.txt")
    count = count_words(word)
    display_top_words(count)
