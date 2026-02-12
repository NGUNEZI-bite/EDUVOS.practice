def: find_word_positions(text, target):
    words = text.split()
    positions = []

    for i, word in enumerate(words):
        if words == target:
            position.append(i + 1)

    return positions

text = "we have alot of fun together, we have less fun when separated but we have each other"
target = "have"
positions = find_word_positions(text, target)
print("positions:", positions)
