with open("anthem.txt", "r") as file:
    lines = file.readlines()

line_count = len(lines)
word_count = sum(len(line.split()) for line in lines)
char_count = sum(len(line) for line in lines)

output = f"Lines: {line_count}\nWords: {word_count}\nCharacters: {char_count}"

with open("anthem_output.txt", "w") as f:
    f.write(output)
