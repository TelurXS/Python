def task1() -> None:
    file = open("name.txt", "w")
    file.write("Yaroslav")
    file.close()
    return


def task2() -> None:
    rows: int = 0
    chars: int = 0

    file = open("text.txt", "w")
    while True:
        value: str = input()

        if value == "":
            break

        file.write(value + "\n")
        rows += 1
        chars += len(value)
    file.close()
    print(f"Rows {rows}")
    print(f"Chars {chars}")
    return


def task3() -> None:
    file = open("poetry.txt", "r")
    lines: list[str] = file.readlines()

    count_without_t: int = 0
    count_with_d: int = 0
    upper_count: int = 0

    for line in lines:

        if not line.startswith("T"):
            count_without_t += 1

        if line.endswith("d"):
            count_with_d += 1

        if line[0].isupper():
            upper_count += 1

    print(f"Count without T: {count_without_t}")
    print(f"Count with d: {count_with_d}")
    print(f"Upper count: {upper_count}")

    return


def task4() -> None:
    file = open("mbox-short.txt", "r")
    lines: list[str] = file.readlines()
    char_count: int = 0
    biggest_word: str = ""

    for line in lines:
        char_count += len(line)

        for word in line.split():
            if len(word) > len(biggest_word):
                biggest_word = word

    print(f"Char count: {char_count}")
    print(f"Biggest word: {biggest_word}")
    return


def task5() -> None:
    file = open("mbox-short.txt", "r")
    lines: list[str] = file.readlines()

    for line in lines:
        print(line.upper(), end="")

    return


def task6() -> None:
    file = open("mbox-short.txt", "r")
    lines: list[str] = file.readlines()
    count: int = 0

    for line in lines:
        if "@" in line:
            print(line, end="")
            count += 1

    print(f"Count: {count}")
    return


def task7() -> None:
    file = open("feedback.txt", "r")
    positive_file = open("positive.txt", "w")
    negative_file = open("negative.txt", "w")
    analysis_file = open("feedback_analysis.txt", "w")
    lines: list[str] = file.readlines()

    total_feedbacks: int = 0
    positive_count: int = 0
    negative_count: int = 0

    for line in lines:
        total_feedbacks += 1

        if line.lower().startswith("positive:"):
            positive_file.write(line)
            positive_count += 1
            continue

        if line.lower().startswith("negative:"):
            negative_file.write(line)
            negative_count += 1
            continue

    analysis_file.write(f"Total feedbacks: {total_feedbacks}\n")
    analysis_file.write(f"Positive feedbacks: {positive_count}\n")
    analysis_file.write(f"Negative feedbacks: {negative_count}\n")
    return


def main() -> None:
    task7()
    return


if __name__ == "__main__":
    main()
