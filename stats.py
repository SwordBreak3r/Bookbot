def word_count(content):
    words = content.split()
    num_words = len(words)
    return num_words

def char_count(content):
    lower = content.lower()
    char_dict = {}
    for char in lower:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_count(char_dict): 
    list = []
    for char in char_dict:
        list.append({"char": char, "num": char_dict[char]})
    list.sort(reverse=True, key=sort_on)
    return list