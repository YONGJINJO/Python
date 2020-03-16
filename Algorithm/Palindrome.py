def is_palindrome(word):
    for count in range(int(len(word) / 2)):
        if word[count] != word[len(word) - count - 1]:
            return False
    return True

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
