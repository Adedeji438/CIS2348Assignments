#PSID:1793979
#ADEDEJI Akingbola


def is_palindrome(string):
    for i in range (0, len(string)//2 + 1):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True

if __name__ == '__main__':
    string = input()
    if is_palindrome(string.strip().replace(" ", "")):
        print(string + " is a palindrome")
    else:
        print(string + " is not a palindrome")