import sys
import string


def to_decrypt(data=None, offset=0):

    """ Decrypting data with Caesar cipher """

    noise = string.punctuation + string.digits
    result = ""

    if data:
        i = 0
        for element in range(len(data)):
            if data[i] in noise:
                result += ""
            elif data[i] == " ":
                result += " "
            else:
                result += chr((ord(data[i]) + offset - 97) % 26 + 97)
            i += 1
        return result
    else:
        return result

if __name__ == "__main__":
    assert to_decrypt() == ""
    assert to_decrypt("!d! [e] &f*", -3) == "a b c"
    assert to_decrypt("x^$# y&*( (z):-)", 3) == "a b c"
    assert to_decrypt("iycfbu!@# junj%&", -16) == "simple text"
    assert to_decrypt("*$#%swzybdkxd !)(^#%dohd", -10) == "important text"
    assert to_decrypt("fgngr **&&frperg^__^", 13) == "state secret"
