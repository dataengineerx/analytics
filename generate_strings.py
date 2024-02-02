def generate_strings(word, current=""):
    if not word:
        print(current)
        return

    for i in range(len(word)):
        new_current = current + word[i]
        new_word = word[:i] + word[i+1:]
        print(f"function call generate_strings({new_word}, {new_current})")
        generate_strings(new_word, new_current)

# Input word
input_word = 'catdog'

# Generate and print all possible strings
generate_strings(input_word)