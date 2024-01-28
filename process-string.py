# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

str = input("Enter a string: ")
result = ''
for letters in str:
    result += letters*2
print (result)

# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.


alphabet = "abcdefghijklmnopqrstuvwxyz"
user_range = input("Enter a range of letters (e.g., a-z): ")

def get_letter_range(range_str):
    start, end = range_str[0], range_str[2]

    start_val = ord(start)
    end_val = ord(end)
    
    # Generate the range of characters
    list_of_letter = []
    for i in range(start_val, end_val + 1):
        list_of_letter.append(chr(i))
    final_answer = "".join(list_of_letter)
    
    return final_answer
