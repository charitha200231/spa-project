sentence = "I kept up with the promise given to my mother"
vowels = "aeiouAEIOU"
vowel_count = sum(1 for c in sentence if c in vowels)
consonant_count = sum(1 for c in sentence if c.isalpha() and c not in vowels)

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
