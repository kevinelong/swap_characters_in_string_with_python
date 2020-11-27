# How to swap two characters in a string with Python

text = "ZBCXYA"


def swap_letters(index1, index2, text):
    data = list(text)
    data[index1], data[index2] = data[index2], data[index1]
    return "".join(data)


# swap first and last (index 0 and -1 respectively)
text = swap_letters(0, -1, text)

print(text)  # "ABCXYZ"
