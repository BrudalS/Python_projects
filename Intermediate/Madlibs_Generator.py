with open("Madlibs Generator Story.txt", "r") as f:
    story = f.read()

word = set()
final_keys = dict()
start_of_word = -1

target_start = "("
target_end = ")"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        words = story[start_of_word: i+1]
        word.add(words)
        start_of_word = -1

for index in word:
    entery = input("Enter the word related to " + index + " ")
    final_keys[index] = entery

for index in word:
    story = story.replace(index, final_keys[index])


print(story)
