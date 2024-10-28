def uncommon_from_sentences(s1, s2):

    word_count = {}

    for word in s1.split():
        word_count[word] = word_count.get(word, 0) + 1

    for word in s2.split():
        word_count[word] = word_count.get(word, 0) + 1

    uncommon_word = []
    for key, value in word_count.items():
        if value == 1:
            uncommon_word.append(key)
        
    return uncommon_word
    

print(uncommon_from_sentences("Ice cream you scream we all scream for ice cream", "Hi how are you"))



