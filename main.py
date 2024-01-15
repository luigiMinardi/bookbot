def get_words_number(text: str) -> int:
    return len(text.split())


def get_characters_count(text: str) -> dict[str,int]:
    t_list = list(text.lower())
    ch_count = {}
    for t in t_list:
        if not t in ch_count:
            ch_count[t] = 0
        ch_count[t] +=1
    return ch_count


def main():
    file_to_open = "books/frankenstein.txt"
    with open(f"{file_to_open}") as f:
        file = f.read()

        print(f"--- Begin report of {file_to_open} ---")
        print(f"{get_words_number(file)} words found in the document\n")

        ch_count = get_characters_count(file)
        alpha_ch_list = [c for c in ch_count if c.isalpha()]
        alpha_ch_list.sort()

        for ch in alpha_ch_list:
            print(f"The {ch} character was found {ch_count[ch]} times")
        print("--- End report ---")


if __name__ == "__main__":
    main()
