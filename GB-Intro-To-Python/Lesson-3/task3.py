# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

import re

text = 'Black Mirror is a British anthology television series created by Charlie Brooker. ' \
       'Individual episodes explore a diversity of genres, but most are set in near-future dystopias ' \
       'with sci-fi technology—a type of speculative fiction. The series is inspired by The Twilight Zone ' \
       'and uses the themes of technology and media to comment on contemporary social issues. ' \
       'Most episodes are written by Brooker with heavy involvement by the executive producer Annabel Jones. ' \
       'There are 27 episodes across six series and one special, in addition to the interactive film Black Mirror: ' \
       'Bandersnatch (2018). The first two series aired on the British network Channel 4 in 2011 and 2013, ' \
       'as did the 2014 special "White Christmas". The programme then moved to Netflix, where four further ' \
       'series aired in 2016, 2017, 2019, and 2023. Two related webisode series were produced by Netflix, ' \
       'and a companion book to the first four series, Inside Black Mirror, was published in 2018. ' \
       'Soundtracks to many episodes have been released as albums. The series has received critical acclaim ' \
       'and is considered by many reviewers to be one of the best television series of the 2010s. ' \
       'The programme won the Primetime Emmy Award for Outstanding Television Movie three times consecutively ' \
       'for "San Junipero", "USS Callister" and Bandersnatch. However, some critics consider the morality of ' \
       'the series obvious or cite declining quality over time. Black Mirror, along with American Horror Story ' \
       'and Inside No. 9, has been credited with repopularising the anthology television format, and a number of ' \
       'episodes have been seen by reviewers as prescient.'

# Используем регулярное выражение для того, чтобы разбить текст на слова
words = re.findall(r'\b\w+\b', text.lower())

# Создаем словарь для подсчета встречаемости слов
word_counts = {}
for word in words:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1

# Сортируем словарь по убыванию количества встречаемости слов и выводим 10 самых частых слов
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
print("The top 10 most frequent words are:")
for word, count in top_words:
    print(f"{word}: {count}")