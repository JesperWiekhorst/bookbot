def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words (text)
    characters = count_characters(text)
    print ("Words in book:", words)
    print ("Characters in book:", characters )

## Gets the text of a book
def get_book_text(path):
    with open(path) as f:
        return f.read()

## counts the words in the book
def count_words(text):
    words = text.split()
    return len(words)

## counts the characters in the book, lowers all characters
def count_characters(text):
    character_dict = {}
    lowered_words = text.lower()
    for char in lowered_words:
        ## Checks if character is alphabetic
        if char.isalpha():
            if char in character_dict:
                 character_dict[char] += 1
            else:
                character_dict[char] = 1
    character_sorted = []
    for key, value in character_dict.items():
        character_sorted.append (f"The '{key}' character was found {value} times")
    # Sort based on the numeric part of the strings
    character_sorted.sort(reverse=True, key=lambda s: int(s.split(' ')[-2]))

    return character_sorted



main()