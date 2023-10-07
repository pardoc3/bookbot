def generate_report(book_path, word_count, letter_count):
    report = []
    # Starting the report
    report.append(f"--- Begin report of {book_path} ---")
    report.append(f"{word_count} words found in the document")
    report.append("")

    # Sorting the letters by their count in descending order
    sorted_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)

    for letter, count in sorted_letters:
        report.append(f"The '{letter}' character was found {count} times")

    # Ending the report
    report.append("--- End report ---")
    return "\n".join(report)


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    word_count = count_words(text)
    letter_count = count_letters(text)
    
    report = generate_report(book_path, word_count, letter_count)
    print(report)


def get_book_text(path):
    with open(path) as f:
        return f.read().lower()


def count_words(text):
    # Assuming words are separated by spaces
    words = text.split()
    return len(words)


def count_letters(text):
    letter_count = {}
    for letter in text:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count


main()
