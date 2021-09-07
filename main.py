# this is required for arguments
import sys

# function to increment character by key
# ord() turns character into its ascii number
# and chr() does the opposite
# the -6 was required to keep those special characters in between the upper- and lowerletter apart
# just take a look on a ascii-table and it will make sense
def change_by(letter: str, key: int):
    if ord(letter) - key < 97:
        return chr(ord(letter) - key - 6)
    else:
        return chr(ord(letter) - key)


# the second argument is the one to encrypt
to_encrypt = str(sys.argv[1]).lower()

# the result for every key
result = ''

# loop truth every key
for key in range(26):
    # loop truth every letter in to_encrypt
    for letter in to_encrypt:

        # dont change spaces
        if letter == ' ':
            result = result + ' '
        else:
            result = result + change_by(letter, key)

    # print the result
    print(str(key) + ": " + result.lower())
    # make the variable ready for the next loop
    result = ''
