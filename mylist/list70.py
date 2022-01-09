def test(lst, char):
    result = [i for i in lst if i.startswith(char)]
    return result
text = ["abcd", "abc", "bcd", "bkie", "cder", "cdsw", "sdfsd", "dagfa", "acjd"]
print("\nOriginal list:")
print(text)
char = "a"
print(test(text, char))
char = "d"
print(test(text, char))
char = "w"
print(test(text, char))
