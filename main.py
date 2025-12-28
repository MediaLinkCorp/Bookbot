from stats import book_num_words
import sys

print("============ BOOKBOT ============")

def get_book_text(filepath):
    with open(filepath) as f:
        print(f"Analyzing book found at {filepath}")
        file_contents = f.read()
        return file_contents

def main():

    if len(sys.argv) >= 2:

        book_num_words(get_book_text(sys.argv[1]))
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
       
main()
print("============= END ===============")