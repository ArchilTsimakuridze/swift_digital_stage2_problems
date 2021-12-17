from collections import Counter

n = int(input())

words = []

for i in range(n):
    word = input()
    words.append(word)

#უნიკალური სიტყვების რაოდენობა
print(len(set(words)))

word_count = Counter(words)

#კონკრეტული სთრინგების რაოდენობა, თანმიმდევრულად
for i in word_count:
    print(word_count[i], end = ' ')
    