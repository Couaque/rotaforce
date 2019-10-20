
#This function is used to display a given array, when we add a certain value to each member of the array
def incrementCharArray(charArray, value):
    res = []

    #For each character in the array given, we add the value provided in the second parameter.
    #We use a modulo because we don't want any character ASCII code be greater than 122.
    #It should go back to 97 instead, which is the ASCII code for the letter A.
    for a in charArray :
        res.append(chr( (ord(a)+value) % 26 + 97))
    #We print the result, and add a second argument to print() in order to avoid the characters to be printed one by line. We want a line to equal a result.
    for c in res :
        print(c, end='')


#This is the function called in our brute.py file, so it is used to call all the other functions.
#This is why it is declared last, because it uses the function declared previously.
def incrementalChar(charString):
    #We convert the array given by the user in an integer array
    #integerArray = stringToIntegerArray(numberString)

    #We add numbers to the array, from 0 to 9. The incrementIntArray will give us the results in the terminal.
    for i in range(ord('a'), ord('z')):
        incrementCharArray(charString, i)
        #When we have a new possible plaintext calculated, we return to the line for more visibility
        print('')

        