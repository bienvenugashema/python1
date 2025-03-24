def chech_palindrome(text):
    text.lower()
    if text == text[::-1]:
        return True
    else:
        return False

print(chech_palindrome("abba"))    
