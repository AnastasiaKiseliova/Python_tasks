import sys

# ///////////////////////////////////////////////////////////////////////////////////////////

def ask_Array():
    try:
        n = [int(s) for s in input().split(' ')]
        return n
    except ValueError:
        print("There are some error in input ↑")


# 1. Easy Unpack //////////////////////////////////////////////////////////////////////////

def easyUnpack(tuple1):
    try:
        return [tuple1[0], tuple1[2], tuple1[-1]]
    except IndexError:
        print('Wrong input')

print('Enter tuple (min 3 elements) :')
tuple2 = ask_Array()

print(easyUnpack(tuple2))

# 2. First Word ///////////////////////////////////////////////////////////////////////////

def firstWord(phrase):
    try:
        space = phrase.index(' ')
        return phrase[0:space + 1]
    except ValueError:
        print('Wrong input')

print('Enter phrase :')
phrase1 = input()

print(firstWord(phrase1))

# 3. Index Power //////////////////////////////////////////////////////////////////////////

def indexPower(array, n):
    result = []
    i = 0
    try:
        for element in array:
            result.append(array[i] ** n)
            i += 1
        return result 

    except IndexError:
        return -1

print('Enter array :')
array1 = ask_Array()
print('Enter N :')
n1 = int(input())

print(indexPower(array1, n1))

# 4. FizzBuzz //////////////////////////////////////////////////////////////////////////////

def fizzBuzz(fb_array):

    i = 0

    try:
        for element in fb_array:
            if(fb_array[i] % 5 == 0 and fb_array[i] % 3 == 0):
                print('FizzBuzz', end = ' ')
                i += 1
            elif(fb_array[i] % 3 == 0):
                print('Fizz', end = ' ')
                i += 1
            elif(fb_array[i] % 5 == 0):
                print('Buzz', end = ' ')
                i += 1
            else:
                i += 1
                continue
            
    except IndexError:
        print('Wrong input')


print('Enter array : ')
fb_array1 = ask_Array()

fizzBuzz(fb_array1)


# ///////////////////////////////////////////////////////////////////////////////////////////