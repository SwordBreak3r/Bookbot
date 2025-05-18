from stats import word_count
from stats import char_count
from stats import sort_count




def get_book_text(file_path):
    string_in_file = str(file_path)
    with open(string_in_file) as f:
        file_contents = f.read()
        return file_contents

def printer(file_path, num_words, sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")  
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for num in sorted:        
        if not num["char"].isalpha():
            continue
        print(f"{num['char']}: {num['num']}")




def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    


    file_path = sys.argv[1]
    contents = get_book_text(file_path)
    num_words = word_count(contents)
    chars = char_count(contents)
    sorted = sort_count(chars)
    printer(file_path, num_words, sorted)

main()
