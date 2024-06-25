def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        words = text.split()
        print(len(words))

main()