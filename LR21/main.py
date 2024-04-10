import os
import shutil
from pathlib import Path

PROJECT_DIR = "./Project_Vats"
TXT_DIR = "./Project_Vats/txt"
CSV_DIR = "./Project_Vats/csv"
COPY_DIR = "./Project_Vats/copy"
DOCS_DIR = "./Project_Vats/docs"


def task1() -> None:
    os.mkdir(PROJECT_DIR)
    os.mkdir(TXT_DIR)
    os.mkdir(CSV_DIR)
    os.mkdir(COPY_DIR)
    os.mkdir(DOCS_DIR)
    return


def task2() -> None:
    for i in range(1, 6):
        path = PROJECT_DIR + f"/{i}.txt"
        with open(path, "w") as file:
            file.write(f"{i}.txt")
    return


def task3() -> None:
    if not os.path.isdir(COPY_DIR):
        os.mkdir(COPY_DIR)

    shutil.copytree(TXT_DIR, COPY_DIR + "/txt")
    return


def task4() -> None:
    for path in os.listdir(TXT_DIR):
        shutil.move(TXT_DIR + "/" + path, DOCS_DIR)
    return


def task5() -> None:
    os.rmdir(TXT_DIR)
    return


def task6() -> None:
    for path in os.listdir(DOCS_DIR):
        os.rename(DOCS_DIR + "/" + path, DOCS_DIR + "/DOCS_FILE_" + path)


def parse_folder(path: Path) -> (list[str], list[str]):
    files: list[str] = []
    directories: list[str] = []

    if not path.exists():
        return files, directories

    if not path.is_dir():
        return files, directories

    for item in path.iterdir():

        if item.is_file():
            files.append(item.name)
            continue

        if item.is_dir():
            directories.append(item.name)
            local_path = path.joinpath(item.name)
            local_files, local_dirs = parse_folder(local_path)
            files.extend(local_files)
            directories.extend(local_dirs)

    return files, directories


def task8() -> None:
    path = Path(PROJECT_DIR)
    print(parse_folder(path))
    return


def main() -> None:
    #task1()
    #task2()
    #task3()
    #task4()
    #task5()
    #task6()
    task8()
    return


if __name__ == "__main__":
    main()
