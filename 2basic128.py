import re
def test(text):
    return re.sub(r'[aeiou]+', '', text, flags=re.IGNORECASE)
text = "Python";
print("Original string:",text)
print("After removing all the vowels from the said string: " + test(text))
text = "C Sharp"
print("\nOriginal string:",text)
print("After removing all the vowels from the said string: " + test(text))
text = "JavaScript"
print("\nOriginal string:",text)
print("After removing all the vowels from the said string: " + test(text))
