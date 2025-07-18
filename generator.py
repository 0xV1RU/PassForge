# # generator.py

# def generate_wordlist(words):
#     print("\n📦 Generating wordlist using provided keywords...\n")

#     patterns = []

#     for word in words:
#         patterns.append(word)
#         patterns.append(word + "123")
#         patterns.append(word + "2025")
#         patterns.append(word + "@123")
#         patterns.append(word.capitalize())
#         patterns.append(word[::-1])
#         patterns.append(word + "!")

#     # Combine all and remove duplicates
#     wordlist = list(set(patterns))

#     with open("wordlist.txt", "w") as f:
#         for word in wordlist:
#             f.write(word + "\n")

#     print(f"✅ Wordlist saved to 'wordlist.txt' ({len(wordlist)} entries)")
import itertools
import random

def leetspeak(word):
    substitutions = {
        'a': ['@', '4'],
        'e': ['3'],
        'i': ['1', '!'],
        'o': ['0'],
        's': ['$', '5'],
        't': ['7'],
        'l': ['1']
    }

    variations = set()
    variations.add(word)

    for i in range(len(word)):
        if word[i].lower() in substitutions:
            for sub in substitutions[word[i].lower()]:
                new_word = word[:i] + sub + word[i+1:]
                variations.add(new_word)

    return list(variations)

def generate_wordlist(keywords):
    print("\n📦 Enhanced Wordlist Generator Started...\n")

    base_variants = []

    special_chars = ['!', '@', '#', '$']
    years = ['2023', '2024', '2025', '123', '321']
    
    for word in keywords:
        variants = [
            word,
            word.capitalize(),
            word.upper(),
            word.lower(),
            word[::-1],
            word + "123",
            word + "@" + "123",
        ]

        # Add leetspeak
        variants += leetspeak(word)

        # Append special chars and years
        for v in variants.copy():
            for y in years:
                variants.append(v + y)
                variants.append(y + v)
            for ch in special_chars:
                variants.append(v + ch)
                variants.append(ch + v)

        base_variants += variants

    # Combine 2-word combos
    combined = []
    for combo in itertools.permutations(keywords, 2):
        combined.append(combo[0] + combo[1])
        combined.append(combo[0].capitalize() + "@" + combo[1])
        combined.append(combo[0] + "_" + combo[1])

    final_list = list(set(base_variants + combined))
    
    # Optional: limit output
    MAX_WORDS = 1000
    if len(final_list) > MAX_WORDS:
        final_list = random.sample(final_list, MAX_WORDS)

    with open("wordlist.txt", "w") as f:
        for word in final_list:
            f.write(word + "\n")

    print(f"✅ Wordlist saved to wordlist.txt with {len(final_list)} entries.\n")
