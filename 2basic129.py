def test(text):
   return [x for x in range(len(text)) if text[x].islower()]
text = "Python";
print("Original string:",text)
print("Indices of all lower case letters of the said string:\n",test(text))
text = "JavaScript";
print("Original string:",text)
print("Indices of all lower case letters of the said string:\n",test(text))
text = "PHP";
print("Original string:",text)
print("Indices of all lower case letters of the said string:\n",test(text))
