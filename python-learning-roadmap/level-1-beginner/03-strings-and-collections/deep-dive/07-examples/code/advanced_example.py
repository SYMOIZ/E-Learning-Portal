from collections import Counter

words = "python python data automation data".split()
frequencies = Counter(words)
print(frequencies.most_common(2))
