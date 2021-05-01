import sys


def words_order(text="", word_list=None):

    """ checks if the word order in the list 
        matches the word order in the text """

    origin_list = text.split()
    current_index = -1
    if text and word_list:
        for element in word_list:
            if element not in origin_list:
                return False
            try:
                index = text.find(element)
                if index > current_index:
                    current_index = index
                    continue
                else:
                    return False
            except ValueError:
                pass
    else:
        return False

    return True

if __name__ == "__main__":
    assert words_order() == False
    assert words_order("a b c", []) == False
    assert words_order("", ['a', 'b', 'c']) == False
    assert words_order("", []) == False
    assert words_order("a b c", ['a', 'b', 'c']) == True
    assert words_order('hi world im here', 
                       ['world', 'here']) == True
    assert words_order('hi world im here', 
                       ['here', 'world']) == False
    assert words_order('hi world im here', 
                       ['world']) == True
    assert words_order('hi world im here', 
                       ['world', 'here', 'hi']) == False
    assert words_order('hi world im here', 
                       ['world', 'im', 'here']) == True
    assert words_order('hi world im here', 
                       ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', 
                       ['world', 'world']) == False
    assert words_order('hi world im here', 
                       ['country', 'world']) == False
    assert words_order('hi world im here', 
                       ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False