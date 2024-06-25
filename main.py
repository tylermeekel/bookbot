def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        lower = text.lower()
        lettersCount = {}
        for char in lower:
            lettersCount[char] = lettersCount.get(char, 0) + 1
        print(lettersCount)

main()