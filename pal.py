def isPalindrome(inputUser):
    palindrome_input = inputUser
    rev = ''.join(reversed(palindrome_input))
    if palindrome_input == rev:
        return True
    return False



# assert palindromeCheck('aba') == 1
