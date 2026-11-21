import sys
import stats


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path/to/book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = stats.get_num_words(text)
    chars_dict = stats.get_chars_dict(text)
    chars_dict_sorted = stats.chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_dict_sorted)

def print_report(path: str, word_count: int, sorted_list: list[tuple[str, int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for element in sorted_list:
        if element[0].isalpha():
            print(f"{element[0]}: {element[1]}")
    print("============= END ===============")

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()
