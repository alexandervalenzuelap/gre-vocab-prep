import json
import random
import os


def save_progress(progress_file, learned_words_file):
    with open(progress_file, 'w') as file:
        file.write(str(current_word_index))

    with open(learned_words_file, 'w') as file:
        file.write('\n'.join(learned_words))


def next_word(progress_file, learned_words_file):
    global current_word_index, current_word
    current_word_index += 1
    if current_word_index < len(words):
        current_word = words[current_word_index]
        print(f"\nNext word: {current_word}")
        print("Definition(s):")
        for meaning in words_data[current_word]['meanings']:
            print(f"- {meaning}")
    else:
        print("You've gone through all the words!")
    save_progress(progress_file, learned_words_file)


def known_word(progress_file, learned_words_file):
    learned_words.append(current_word)
    next_word(progress_file)


def revise(progress_file, learned_words_file):
    random.shuffle(learned_words)
    if learned_words:
        word_to_revise = learned_words.pop()
        print(f"Revise: {word_to_revise}")
    else:
        print("You've revised all the learned words!")
    save_progress(progress_file, learned_words_file)


# Create a directory to store progress if it doesn't exist
progress_folder = 'gre_progress'
if not os.path.exists(progress_folder):
    os.makedirs(progress_folder)

words_json = 'words.json'
progress_file = os.path.join(progress_folder, 'progress.txt')
learned_words_file = os.path.join(progress_folder, 'learned_words.txt')

# Load words from the JSON file
with open(words_json, 'r') as file:
    words_data = json.load(file)

# Sort words based on frequency
words = sorted(
    words_data, key=lambda x: words_data[x]['frequency'], reverse=True)

# Initialize variables
current_word_index = 0
learned_words = []

# Create a directory to store progress if it doesn't exist
progress_folder = 'gre_progress'
if not os.path.exists(progress_folder):
    os.makedirs(progress_folder)

progress_file = os.path.join(progress_folder, 'progress.txt')
learned_words_file = os.path.join(progress_folder, 'learned_words.txt')

if os.path.exists(progress_file):
    with open(progress_file, 'r') as file:
        current_word_index = int(file.read())

if os.path.exists(learned_words_file):
    with open(learned_words_file, 'r') as file:
        learned_words = file.read().splitlines()


# GRE Word Learning Interface
while current_word_index < len(words):
    print("\nGRE Word Learning Menu")
    print("1. Show next word")
    print("2. Mark as known")
    print("3. Revise learned words")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        next_word(progress_file, learned_words_file)
    elif choice == '2':
        known_word(progress_file, learned_words_file)
    elif choice == '3':
        revise(progress_file, learned_words_file)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a number between 1-4.")

print("Thank you for using GRE Word Learning program!")
