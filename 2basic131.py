def test(num):
    ones =  bin(num). replace("0b", "").count('1')
    zeros = bin(num). replace("0b", "").count('0')
    return "Number of zeros: " + str(zeros) + ", Number of ones: " + str(ones);

n = 12;
print("Original number: ",n);
print("Number of ones and zeros in the binary representation of the said number:");
print(test(n));
n = 1234;
print("\nOriginal number: ",n);
print("Number of ones and zeros in the binary representation of the said number:");
print(test(n));
