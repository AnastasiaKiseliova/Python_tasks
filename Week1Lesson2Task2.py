# /////////////////////////////////////////////////////////////////////////////////////

print('enter nubers (each one on the next line / press enter to exit)')

numbers = []

# /////////////////////////////////////////////////////////////////////////////////////

while True:
    x = input()
    if (x != ''):
        try:
            numbers.append(int(x))
        except ValueError:
            print('its not a number. try again')
            continue
    else:
        break

# /////////////////////////////////////////////////////////////////////////////////////

print('numbers:', end=' ')

for i in numbers:
    print(i, end=' ')

# /////////////////////////////////////////////////////////////////////////////////////

print('quantity: ', len(numbers))

# /////////////////////////////////////////////////////////////////////////////////////

sum = 0

for i in numbers:
    sum += i

print('sum: ', sum)

# /////////////////////////////////////////////////////////////////////////////////////

min = float('inf')
max = float('-inf')

for i in numbers:
    if(i < min):
        min = i

for i in numbers:
    if(i > max):
        max = i

print('min: ', min, 'max: ', max)

# /////////////////////////////////////////////////////////////////////////////////////

print('average value: ', sum / len(numbers))

# /////////////////////////////////////////////////////////////////////////////////////

def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
    res = []
    for i in range(len(arr)): 
         res.append(arr[i])

    return res

print('sorted array: ', bubbleSort(numbers))

# /////////////////////////////////////////////////////////////////////////////////////

median = 0

if(len(numbers) % 2 == 0):
    median = (numbers[(len(numbers)//2)] + numbers[(len(numbers)//2 - 1)]) / 2
else:
    median = numbers[len(numbers)//2 - 1]

print('median: ', median)

# /////////////////////////////////////////////////////////////////////////////////////