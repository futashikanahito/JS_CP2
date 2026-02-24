# ----- PSEUDOCODE -----
# organize(): Open file, strip word count footer if present, return word count
# append(): Format word count + timestamp as footer text, append to file
# main_text(): Open file, strip word count footer if present, return cleaned text

# ----- CODE & PSEUDOCODE -----
# Pseudocode for organize():
# - Open and read the file
# - If a "Word Count:" section exists, discard it and everything after
# - Split remaining text into words and return the count
def organize(current_file):
    with open(current_file, "r") as file:
        text = file.read()

    if "Word Count:" in text:
        text = text.split("Word Count:")[0]

    return len(text.split())

# Pseudocode for append():
# - Build a footer string with the word count and timestamp
# - Open the file in append mode and write the footer
def append(current_file, word_count, time):
    text = f"\n\nWord Count: {word_count}\nLast Updated: {time}"

    with open(current_file, "a") as file:
        file.write(text)

# Pseudocode for main_text():
# - Open and read the file
# - If a "Word Count:" section exists, discard it and everything after
# - Strip trailing whitespace and return the clean main text
def main_text(current_file):
    with open(current_file, "r") as file:
        text = file.read()

    if "Word Count:" in text:
        text = text.split("Word Count:")[0]

    return text.rstrip()