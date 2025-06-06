def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

input_str = "Madam"
print(f"{input_str} is palindrome:", is_palindrome(input_str))
