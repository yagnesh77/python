def test(str1):
    return ''.join(sorted(str1))

str1 = "PHP"
print("Original string:",str1)
print("Convert the letters of the said string into alphabetical order:",test(str1))
str1 = "javascript"
print("\nOriginal string:",str1)
print("Convert the letters of the said string into alphabetical order:",test(str1))
str1 = "python"
print("\nOriginal string:",str1)
print("Convert the letters of the said string into alphabetical order:",test(str1))
