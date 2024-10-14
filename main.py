def main():
    book = "books/frankenstein.txt"
    
    words = get_book_content(book)
    
    chars = count_chars(words)
    
    sorted_list = chars_sorted_list(chars)
    print(f"--- Begin report of {book} ---")
    print(f"{count_words(words)} words found in the document")
    print("\n")
    
    
    # sortd.sort(reverse=True)
    for i in sorted_list:
        if not i["char"].isalpha():
            continue
        print(f"The '{i['char']}' character was found {i['num']} times")
    
    print("-- End report --")
        

def get_book_content(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def count_chars(text):
    chars = {}
    for i in text:
       lowered = i.lower()
       
       if lowered not in chars:
           chars[lowered] = 1
       else:
           chars[lowered] += 1
        
    return chars

def count_words(words):
    count = words.split()
    return len(count)

def sort_on(dit):
    return dit["num"]

def chars_sorted_list(chars):
    sorted_list = []
    for c in chars:
        sorted_list.append({"char": c, "num": chars[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
