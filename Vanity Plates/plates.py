
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return number_of_letters(s) and first_two(s) and word_characters(s) and end_w_number(s)

#start with at least two letters
def first_two(s):
    if s[0:2].isalpha():
        return s

#maximum of 6 characters (letters or numbers) and a minimum of 2 characters
def number_of_letters(s):
    if 2 <= len(s) <= 6:
        return s

#Numbers cannot be used in the middle of a plate
#first number used cannot be a ‘0’
def end_w_number(s):
    index = []
    for i, c in enumerate(s):
        if c.isdigit():
            index.append(i)
    if index:
        char = s[0:index[0]]
        digit = s[index[0]:]
        if s == char + digit and digit.isdigit() and len(char) >= 2 and digit.startswith("0") == False:
            return s
    else:
        char = s
        if s == char and len(char) >= 2:
            return s

#No periods, spaces, or punctuation
def word_characters(s):
    return s.isalnum()


if __name__ == "__main__":
    main()


