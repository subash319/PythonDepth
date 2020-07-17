# 7. In the exercise on loops, we had written a program to count frequency of each word in a string.
# Now write a program to count frequency of each word in a file.

word_comp = 'small'
with open('comp1.txt', 'r') as fr:
    # count = 0
    # for line in fr:
    #     for word in line.split():
    #         if word.lower() == word_comp:
    #             count += 1
    # print(f"count of the word {word_comp} is {count} ")
    count = {}
    for word in fr.read().split():
        count[word] = count.get(word, 0) + 1
    print(count)