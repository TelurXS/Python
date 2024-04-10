import os


def new_file(name: str, content: str) -> None:
    with open(name, "x") as file:
        file.write(content)
    return


def rename_file(source: str, name: str) -> None:
    os.rename(source, name)
    return


def delete_file(name: str) -> None:
    os.remove(name)
    return


def task7() -> None:
    while True:
        print("new - create file")
        print("rename - rename file")
        print("delete - delete file")

        action = input("Select action: ")

        match action:
            case "new":
                name = input("Input file name: ")
                content = input("Input file content: ")
                new_file(name, content)

            case "rename":
                source = input("Input source name: ")
                name = input("Input file new name: ")
                rename_file(source, name)

            case "delete":
                name = input("Input file name: ")
                delete_file(name)

            case "exit":
                break
    return


def main() -> None:
    task7()
    return


if __name__ == "__main__":
    main()
