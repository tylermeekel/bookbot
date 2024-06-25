def sort_on(dict):
    return dict["num"]

def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        lower = text.lower()

        words = lower.split()
        num_words = len(words)

        lettersCount = {}
        # create a dictionary of letters and their counts
        for word in words:
            for char in word:
                if char.isalpha():
                    lettersCount[char] = lettersCount.get(char, 0) + 1

        # convert to list of dicts
        lettersList = []
        for letter, count in lettersCount.items():
            lettersList.append({"letter": letter, "num": count})
        
        # sort the list of dicts
        lettersList.sort(key=sort_on, reverse=True)

        # print the report
        print("-- Begin report of books/frankenstein.txt --")
        print(f"{num_words} found in the document.")
        for item in lettersList:
            print(f"The letter '{item['letter']}' was found {item['num']} times")
        print("-- End report --")

main()