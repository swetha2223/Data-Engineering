def capitalize_words(s):
    return str.upper(s)

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    s=str.lower(s)
    count=0
    vowels=set('aeiou')
    for c in s:
        if c in vowels:
            count+=1
    return count

def is_palindrome(s):
    s2=reverse_string(s)
    return s2==s