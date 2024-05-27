def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowerWords = file_contents.lower()

    letter_count = {}
    for i in lowerWords:
        for char in i:
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    for key,val in letter_count.items():
        print(f"The '{key}' character was found {val} times")
main()
