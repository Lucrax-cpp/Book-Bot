def get_num_words(text:str)->int:
    #Splits the words
    words=text.split()
    #Counts and returns the output
    return len(words)


def get_chars_dict(text:str)->dict[str,int]:
    chars={}
    #It checks for every character in the book
    for c in text:
        #It lowers it
        lowered=c.lower()
        if lowered in chars:
            #If the character already is defined it adds one to it
            chars[lowered]+=1
        else:
            #If the character isn't defined it adds it with the value 1
            chars[lowered]=1
    return chars

def sort_on(tuple:tuple[str,int])->int:
    #It just prints the int of the tuple
    return tuple[1]

def chars_dict_to_sorted_list(dictionary:dict[str, int])->list[tuple[str,int]]:
    tuple_list=list(dictionary.items())
    x=sorted(tuple_list, key=sort_on, reverse=True)
    return x
