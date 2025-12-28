def book_num_words(book_text):
    book_words = []

    book_words = len(book_text.lower().split())

    result = f"Found {book_words} total words"
    print("----------- Word Count ----------")
    print(result)

    words_to_chars(book_text.split())

    return result

def words_to_chars(book_text):
    word_count={}

    for words in book_text:
        for letters in words:
            letter_lower = letters.lower()
            if letter_lower in word_count:
                word_count[letter_lower] += 1
            else:
                word_count[letter_lower] = 1
    #print( word_count)
    report(word_count)

def report(characters):

    sorted_list_dict = []
    
    for key in characters:
        dict_item = {}
        dict_item["char"]=key
        dict_item["num"]=characters[key]


        sorted_list_dict.append(dict_item)
    
    sorted_list_dict.sort(key=lambda x: x["num"],reverse=True)

    print("--------- Character Count -------")

    for key in sorted_list_dict:
        if key["char"].isalpha():
            print(f"{key["char"]}: {key["num"]}")

    return sorted_list_dict


            

  
