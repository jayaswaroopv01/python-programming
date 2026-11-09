j="w3coder"
vowels=sum(1 for c in j.lower()if c in "aeiou")
consonants=sum(1 for c in j.lower()if c.isalpha()and c not in"aeiou")
print(f"vowels:{vowels},consonants:{consonants}")
